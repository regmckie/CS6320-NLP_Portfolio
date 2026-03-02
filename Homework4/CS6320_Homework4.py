# FILENAME: CS6320_Homework4.py
# DUE DATE: 10/8/2024
# AUTHOR:   Reg Gonzalez
# EMAIL:    rdg170330@utdallas.edu (school) or regmckie@gmail.com (personal)
# COURSE:   CS 6320.002, Fall 2024

# This file is for Problem 3 of Homework 4.

# ********************************************************************************
# * PROBLEM 3:                                                                   *
# * Using rdflib (open-source Python library), load the RDF into the graph       *
# * and run the same SPARQL query [from Problem 2].                              *
# ********************************************************************************

from rdflib.namespace import OWL, RDF, XSD
from rdflib import Namespace, Graph, Literal

# Create a graph for the RDF file and load it in
graph = Graph()
graph.parse("CS6320_HW4_Ontology.rdf")

# Define namespaces
CS6320_HW4 = Namespace("http://www.semanticweb.org/regmc/ontologies/2024/9/cs6320_hw4#")
graph.bind("cs6320_hw4", CS6320_HW4)
graph.bind("owl", OWL)
graph.bind("rdf", RDF)
graph.bind("xsd", XSD)

# Define SPARQL query we used in Problem 2
# The query asks "What is the legal drinking age and what is Jane's age?"
sparql_query = """
PREFIX cs6320_hw4: <http://www.semanticweb.org/regmc/ontologies/2024/9/cs6320_hw4#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

SELECT ?legalDrinkingAge ?janeAge
WHERE {
  # Retrieve Jane's age
  cs6320_hw4:Jane cs6320_hw4:hasAge ?janeAge .
  
  # Retrieve the legal drinking age from the LegalDrinker class
  ?restriction owl:onProperty cs6320_hw4:hasAge ;
               owl:someValuesFrom ?dataType .
  ?dataType owl:onDatatype xsd:int ;
            owl:withRestrictions ?restrictionList .
  ?restrictionList rdf:rest*/rdf:first ?restrictionItem .
  ?restrictionItem xsd:minInclusive ?legalDrinkingAge .
}
"""

# Execute SPARQL query and print out its results
results = graph.query(sparql_query)
for r in results:
    print(f"Legal Drinking Age: {r.legalDrinkingAge}, Jane's Age: {r.janeAge}")
