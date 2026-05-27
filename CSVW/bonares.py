import json
import argparse
from pathlib import Path


# ============================================================
# CSVW CONTEXT
# ============================================================

CONTEXT = {
    "@vocab": "http://www.w3.org/ns/csvw#",
    "csvw": "http://www.w3.org/ns/csvw#",
    "dc": "http://purl.org/dc/terms/",
    "sosa": "http://www.w3.org/ns/sosa/",
    "qudt": "http://qudt.org/schema/qudt/",
    "unit": "http://qudt.org/vocab/unit/"
}


# ============================================================
# DATATYPE MAPPING
# ============================================================

def map_datatype(bonares_type):
    """
    Convert BoNaRes datatype -> CSVW datatype.
    """

    if not bonares_type:
        return "string"

    t = bonares_type.lower()

    if "int" in t:
        return "integer"

    if "float" in t or "double" in t or "decimal" in t:
        return "number"

    if "date" in t:
        return "date"

    if "time" in t:
        return "datetime"

    if "bool" in t:
        return "boolean"

    return "string"


# ============================================================
# UNIT MAPPING
# ============================================================

UNIT_MAP = {
    "kg": "unit:KiloGM",
    "g": "unit:GM",
    "mg": "unit:MilliGM",
    "cm": "unit:CentiM",
    "m": "unit:M",
    "%": "unit:PERCENT"
}


def map_unit(unit_string):

    if not unit_string:
        return None

    key = unit_string.strip().lower()

    return UNIT_MAP.get(key)


# ============================================================
# SOSA ANNOTATIONS
# ============================================================

def create_sosa_annotations(attr):

    annotations = {}

    # observed property
    description = attr.get("description", "").strip()

    if description:
        prop_name = description.replace(" ", "_")
        annotations["sosa:observedProperty"] = {
            "@id": f"http://example.org/observedProperty/{prop_name}"
        }

    # observation procedure
    methods = attr.get("methods", "").strip()

    if methods:
        method_name = methods.replace(" ", "_")
        annotations["sosa:usedProcedure"] = {
            "@id": f"http://example.org/procedure/{method_name}"
        }

    # unit
    unit_uri = map_unit(attr.get("unit", ""))

    if unit_uri:
        annotations["qudt:unit"] = {
            "@id": unit_uri
        }

    return annotations


# ============================================================
# BUILD COLUMN
# ============================================================

def build_column(attr):

    column = {
        "name": attr.get('name',''),
        "titles": attr.get('name',''),
        "datatype": map_datatype(attr.get("dataType")),
        "dc:description": attr.get("description", "")
    }

    missing = attr.get("missingValue")

    if missing and missing.lower() != "no missing values":
        column["null"] = [missing]

    # Add SOSA/QUDT annotations
    column.update(create_sosa_annotations(attr))

    return column


# ============================================================
# FOREIGN KEYS
# ============================================================

def extract_foreign_keys(attributes):

    foreign_keys = []

    for key, attr in attributes.items():
        if 'datamodelAttribute' in key: 
            source_column = attr["name"]

            for key, value in attr.items():

                if key.startswith("foreignKey_"):

                    target_table = value["table"]

                    fk = {
                        "columnReference": source_column,
                        "reference": {
                            "resource": f"{target_table}.csv",
                            "columnReference": value["column"]
                        }
                    }

                    foreign_keys.append(fk)

    return foreign_keys


# ============================================================
# FIND METADATA FILE
# ============================================================

def find_metadata_file(csv_file):
    """
    Finds metadata JSON corresponding to a CSV file.

    Example:
        mytable.csv -> mytable.json
    """

    json_file = csv_file.with_suffix(".bonares.json")

    if json_file.exists():
        return json_file

    return None


# ============================================================
# BUILD TABLE
# ============================================================

def build_table(csv_file, metadata_file):

    with open(metadata_file, "r", encoding="utf-8") as f:
        metadata = json.load(f)

    attrs = metadata["bonaresInfo"]

    columns = []

    for key, attr in attrs.items():
        if 'datamodelAttribute' in key:
            columns.append(build_column(attr))

    table = {
        "url": csv_file.name,
        "tableSchema": {
            "columns": columns
        }
    }

    # Foreign keys
    foreign_keys = extract_foreign_keys(attrs)

    if foreign_keys:
        table["tableSchema"]["foreignKeys"] = foreign_keys

    return table


# ============================================================
# MAIN CONVERSION
# ============================================================

def convert_folder_to_csvw(folder_path, output_file="csv-metadata.json"):

    folder = Path(folder_path)

    if not folder.exists():
        raise FileNotFoundError(f"Folder does not exist: {folder}")

    tables = []

    csv_files = list(folder.glob("*.csv"))

    print(f"Found {len(csv_files)} CSV files")

    for csv_file in csv_files:

        metadata_file = find_metadata_file(csv_file)

        if not metadata_file:
            print(f"Skipping {csv_file.name} (no metadata JSON found)")
            continue

        print(f"Processing {csv_file.name}")

        table = build_table(csv_file, metadata_file)

        tables.append(table)

    csvw = {
        "@context": CONTEXT,
        "tables": tables
    }

    output_path = folder / output_file

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(csvw, f, indent=2)

    print(f"\nCSVW metadata written to:")
    print(output_path)


# ============================================================
# CLI
# ============================================================

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Convert BoNaRes TableSchema metadata to CSVW"
    )

    parser.add_argument(
        "folder",
        help="Folder containing CSV files and matching JSON metadata files"
    )

    parser.add_argument(
        "--output",
        default="csv-metadata.json",
        help="Output CSVW metadata filename"
    )

    args = parser.parse_args()

    convert_folder_to_csvw(args.folder, args.output)