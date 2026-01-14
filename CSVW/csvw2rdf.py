#!/usr/bin/env python3
"""
csv_to_jsonld_csvwlib.py
Convert a CSV + CSVW metadata file into JSON-LD using csvwlib.
"""

import argparse
from csvwlib import CSVWConverter
import rdflib

def convert(csv_path=None, metadata_path=None, mode="standard", format="json-ld"):
    # Run csvwlib conversion
    graph = CSVWConverter.to_rdf(csv_path, metadata_path, mode=mode)
    # Ensure result is an rdflib.Graph
    if not isinstance(graph, rdflib.Graph):
        raise RuntimeError("csvwlib did not return an rdflib.Graph")
    return graph.serialize(format=format)

def main():
    parser = argparse.ArgumentParser(description="Convert CSV + metadata to JSON-LD with csvwlib")
    parser.add_argument("--csv", "-c", help="Path or URL to CSV file (optional if metadata references it)")
    parser.add_argument("--meta", "-m", help="Path or URL to CSVW metadata JSON")
    parser.add_argument("--out", "-o", help="Output JSON-LD file (default: print to stdout)")
    parser.add_argument("--mode", default="minimal", choices=["standard", "minimal"],
                        help="CSVW conversion mode")
    parser.add_argument("--format", "-f", default="json-ld", help="A rdf format to serialize", 
                        choices=["json-ld","xml","n3","nt","ttl","trig","nquads"])
    args = parser.parse_args()

    myrdf = convert(args.csv, args.meta, mode=args.mode, format=args.format)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(myrdf)
        print(f"✔ Wrote rdf to {args.out}")
    else:
        print(myrdf)


if __name__ == "__main__":
    main()
