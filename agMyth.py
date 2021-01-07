from franz.openrdf.connect import ag_connect
from franz.openrdf.query.query import QueryLanguage
from franz.openrdf.rio.rdfformat import RDFFormat
import os.path
#https://franz.com/agraph/support/documentation/current/python/tutorial/example003.html#
with ag_connect('Mythologie', host='localhost', port='10035',
                user='Marc', password='marc') as conn:
   print ("Total = %s triples" % (conn.size()))
   query_string = "select ?g (count(?s) as ?tot) where {GRAPH ?g {?s ?p ?o}} group by ?g"
   tuple_query = conn.prepareTupleQuery(QueryLanguage.SPARQL, query_string)
   result = tuple_query.evaluate()

with result:
   for binding_set in result:
        g = binding_set.getValue("g")
        tot = binding_set.getValue("tot")
        print("GRAPH %s %s " % (g, tot))

DATA_DIR = 'data'
path0 = os.path.join(DATA_DIR, 'skos.rdf')
context0 = conn.createURI("http://www.w3.org/mythologie/skoscore")
path1 = os.path.join(DATA_DIR, 'mythologie.ttl')
context1 = conn.createURI("http://www.w3.org/mythologie/metamodel")
#conn.addData(event)
path2 = os.path.join(DATA_DIR, 'mythologie_god.json')
context2 = conn.createURI("http://www.w3.org/mythologie/gods")
path3 = os.path.join(DATA_DIR, 'mythologie_human.json')
context3 = conn.createURI("http://www.w3.org/mythologie/mortals")
path4 = os.path.join(DATA_DIR, 'mythologieTemple.json')
context4 = conn.createURI("http://www.w3.org/mythologie/temples")
path5 = os.path.join(DATA_DIR, 'mythologiePlants.json')
context5 = conn.createURI("http://www.w3.org/mythologie/plants")
path6 = os.path.join(DATA_DIR, 'mythologieGeo.json')
context6 = conn.createURI("http://www.w3.org/mythologie/geography")
path7 = os.path.join(DATA_DIR, 'mythologieCreatures.json')
context7 = conn.createURI("http://www.w3.org/mythologie/creatures")
path8 = os.path.join(DATA_DIR, 'mythologieAuthor.json')
context8 = conn.createURI("http://www.w3.org/mythologie/authors")
path9 = os.path.join(DATA_DIR, 'mythologieSymbol.json')
context9 = conn.createURI("http://www.w3.org/mythologie/symbols")

with ag_connect('Mythologie', host='localhost', port='10035',
                user='Marc', password='marc', clear=True) as conn:
    conn.addFile(path0, None, format=RDFFormat.RDFXML, context=context0)
    conn.addFile(path1, None, format=RDFFormat.TURTLE, context=context1)
    conn.addFile(path2, None, context=context2)
    conn.addFile(path3, None, context=context3)
    conn.addFile(path4, None, context=context4)
    conn.addFile(path5, None, context=context5)
    conn.addFile(path6, None, context=context6)
    conn.addFile(path7, None, context=context7)
    conn.addFile(path8, None, context=context8)
    conn.addFile(path9, None, context=context9)
    print('Metamodel triples (in {context}): {count}'.format(
      count=conn.size(context1), context=context1))
    print ("Total = %s triples" % (conn.size()))