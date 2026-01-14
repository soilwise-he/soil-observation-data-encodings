from rdflib import Graph, Namespace, BNode, URIRef, Literal
from rdflib.namespace import RDF, RDFS, XSD, SKOS, DCTERMS
import sqlite3, sys
import json, shutil, hashlib
from datetime import datetime

# --- Config ---
RDF_FORMAT = "turtle"           # "xml", "nt", "json-ld" etc.
shutil.copyfile("./iso28258.sqlite", "export.sqlite")
database = "export.sqlite"

# Namespaces
SOSA = Namespace("http://www.w3.org/ns/sosa/")
GEO  = Namespace("http://www.opengis.net/ont/geosparql#")
WGS  = Namespace("http://www.w3.org/2003/01/geo/wgs84_pos#")
QUDT = Namespace("http://qudt.org/schema/qudt/")

# ---- Helpers ----
def bn_to_urn(node):
    """Create a stable URN for a Blank Node or non-URI node."""
    s = str(node)
    h = hashlib.sha1(s.encode("utf-8")).hexdigest()
    return f"urn:bn:{h}"

def node_to_uri(node):
    """Return a stable string identifier for a node (URI or BNode)."""
    if isinstance(node, URIRef):
        return str(node)
    if isinstance(node, BNode):
        return bn_to_urn(node)
    if isinstance(node, Literal):
        return str(node)
    return str(node)

def first_value(g, subject, predicate):
    """Return the first value for subject predicate or None (as python object)."""
    v = next(g.objects(subject, predicate), None)
    if v is None:
        return None
    # For rdflib LITERAL / URIRef return python value appropriately
    if isinstance(v, Literal):
        return str(v)
    return v  # keep URIRef or BNode for further lookup

def label_for(g, node):
    """Prefer rdfs:label, then skos:prefLabel if present, else the URI / bnode string."""
    if node is None:
        return None
    lab = first_value(g, node, RDFS.label) or first_value(g, node, SKOS.prefLabel) or first_value(g, node, DCTERMS.title)
    if lab:
        return str(lab)
    # fallback to node's string/uri
    return node_to_uri(node)

def get_pref_labels_from_remote(concept_uri):
    g = Graph()
    # rdflib will try to GET the resource and parse it (it guesses format)
    try:
        g.parse(concept_uri)  # remove format if server may return another RDF format
        uri = URIRef(concept_uri)
        return list(g.objects(uri, SKOS.prefLabel))
    except Exception as ex:
        print('failed get prefLabel for skos term',concept_uri,ex)

def types_text_for(g, node):
    """
    Return a text representation for rdf:type values on `node`.
    - Return comma-joined localnames of the types (e.g. 'Feature,Profile').
    - Returns None if no types found.
    """
    types = list(g.objects(node, RDF.type))
    if not types:
        return None

    # fallback: collect localnames or full URIs if localname not available
    def localname(uri):
        s = str(uri)
        if "#" in s:
            return s.split("#", 1)[1]
        if "/" in s:
            return s.rsplit("/", 1)[1]
        return s

    names = []
    for t in types:
        if isinstance(t, URIRef):
            names.append(localname(t))
        else:
            names.append(str(t))
    return ",".join(names)

# utility upsert functions returning row id
def upsert_single_return_id(table, uri, label=None, extra_col=None, extra_val=None):
    """
    Generic insert-or-ignore then select id. If extra_col/extra_val provided, include in insert.
    """
    if uri is None:
        return None
    if extra_col:
        sql_ins = f"INSERT OR IGNORE INTO {table} (uri, label, {extra_col}) VALUES (?, ?, ?)"
        cur.execute(sql_ins, (uri, label, extra_val))
    else:
        cur.execute(f"INSERT OR IGNORE INTO {table} (uri, label) VALUES (?, ?)", (uri, label))
    cur.execute(f"SELECT {table}_id FROM {table} WHERE uri = ?", (uri,))
    row = cur.fetchone()
    return row[0] if row else None

g = None
# --- Load RDF ---
try:
    RDF_FILE = sys.argv[1]   # your RDF file
    g = Graph()
    g.parse(RDF_FILE, format=RDF_FORMAT)
    print(f"Loaded {len(g)} triples from {RDF_FILE}")
except:
    print('provide ttl file to parse')
    quit()

with sqlite3.connect(database) as conn:
    cur = conn.cursor()

    if 1==1: # try:
        # iterate over explicit observation subjects
        obs_count = 0
        for obs in g.subjects(RDF.type, SOSA.Observation):
            obs_count += 1
            obs_uri = node_to_uri(obs)
            # Phenomenon time (literal)
            phen_time = None
            phen_time2 = first_value(g, obs, SOSA.phenomenonTime) or first_value(g, obs, SOSA.phenomenon_time) or first_value(g, obs, SOSA.resultTime)
            if phen_time2:
                try:    
                    dt = datetime.strptime(phen_time2.split('T')[0], "%Y-%m-%d")
                    phen_time = dt.timestamp()
                except:
                    print('can not date parse',phen_time2.split('T')[0])
            # result text (simple literal)
            qual_value_text = first_value(g, obs, SOSA.hasSimpleResult)
            # qualitative value node (may be blank node or URI)
            qual_node = first_value(g, obs, SOSA.result) or first_value(g, obs, SOSA.hasResult)
            qual_uri = None
            qual_label = None
            qual_value_text = None
            if qual_node is not None:
                # if it's a node (URIRef/BNode), create stable id
                qual_uri = node_to_uri(qual_node) if not isinstance(qual_node, Literal) else None
                # label or text
                qual_label = label_for(g, qual_node) if qual_uri else str(qual_node)
                # maybe the observation also has a simple result we should preserve as value_text
                qual_value_text = first_value(g, qual_node, QUDT.numericValue) or first_value(g, qual_node, QUDT.quantityValue) 
                # unit (might be linked via qudt or as property on observation)
                unit_node = first_value(g, qual_node, QUDT.unit) or first_value(g, obs, QUDT.unit)
                unit_uri = node_to_uri(unit_node) if unit_node is not None else None
                unit_label = label_for(g, unit_node) if unit_node is not None else None
            # procedure
            proc_node = first_value(g, obs, SOSA.usedProcedure) or first_value(g, obs, SOSA.isProducedBy)
            proc_uri = node_to_uri(proc_node) if proc_node is not None else None
            proc_label = label_for(g, proc_node) if proc_node is not None else None
            # observed property
            prop_node = first_value(g, obs, SOSA.observedProperty) or first_value(g, obs, SOSA.hasObservedProperty)
            prop_uri = node_to_uri(prop_node) if prop_node is not None else None
            prop_label = label_for(g, prop_node) if prop_node is not None else None
            # feature of interest
            foi_node = first_value(g, obs, SOSA.hasFeatureOfInterest) or first_value(g, obs, SOSA.featureOfInterest)
            foi_uri = node_to_uri(foi_node) if foi_node is not None else None
            foi_label = label_for(g, foi_node) if foi_node is not None else None
            foi_type = types_text_for(g, foi_node)
            # geometry text
            # geom_text = get_geometry_text(g, foi_node) if foi_node is not None else None

            # Upsert referenced entities and get ids
            proc_id = upsert_single_return_id("procedure", proc_uri, proc_label)
            unit_id = upsert_single_return_id("unitofmeasure", unit_uri, unit_label)
            prop_id = upsert_single_return_id("property", prop_uri, prop_label)
            foi_id = upsert_single_return_id("feature_of_interest", foi_uri, foi_type)
            if qual_value_text not in [None, '']:
                UPSERT_RES = f"INSERT INTO result (result_uri,value,unit_of_measure_id) VALUES (?, ?, ?)"
                cur.execute(UPSERT_RES,(qual_uri,qual_value_text,unit_id))

            UPSERT_OBS = """
            INSERT INTO observation (observation_uri, result_uri, phenomenon_time, procedure_id, property_id, foi_id)
            VALUES (?, ?, ?, ?, ?, ?)
            """
            cur.execute(UPSERT_OBS,(obs_uri, qual_uri, phen_time, proc_id, prop_id, foi_id))
             
        conn.commit()
        print("Data loaded")
    #except Exception as e:
    #    print('error',e)
    #finally: 
        cur.close()

    