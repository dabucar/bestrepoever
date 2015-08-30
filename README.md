# bestrepoever

## Current goals

Create a protein-protein extraction pipeline/program.

According to prior discussions we are trying to use Medline/Pubmed
documents as inputs to our pipeline. What we want to do with the extracted
relations is not yet completely clear but the main ideas were to 1. put
them into ElasticSearch for search and/or 2. into a graph DB like
[Neo4J](http://neo4j.com/) or [Cayley](https://github.com/google/cayley)
for further exploratory experimentation.


## Possible pipeline design

[XML articles] --> [Python script extracts indexable text] --> [sentence detection * ] --> [tokenization * ] --> [POS tagging * ] --> [parsing * ] --> [named entity recognition ([OpenNer](http://www.opener-project.eu/))] --> [relation extraction ([Stanford Relation Extractor](http://nlp.stanford.edu/software/relationExtractor.shtml)?)] --> [feed to ElasticSearch/GraphDB]

* Using openNLP, ClearNLP, NLTK...

Some thoughts:

It may be better to just do named entity recognition (NER) without any
parsing/pos tagging (if it is not required by the NER approach we use)
as a first step. Doing relation ship extraction can then be added later
including all the NLP steps that I assume will be needed.

Choosing the way to represent relations in order for them to be searchable
in ElasticSearch/GraphDBs is non-trivial. Depending on the approach we
choose we will have to add more text-format-changing scripts as well.

Having POS tags and being able to use them in queries would be very
interesting, especially together with the ability to specify objects of
verbs to search for. If we can add the ability to search for hierarchical
vocabularies we would be on feature parity with commercial "text mining
solutions." These goals can be tackled at a later stage though.
