from __future__ import print_function

''' ain't nobody got time fo wait '''
''' XML extraction v0.0.0.0.1 '''
''' dabucar 2015-08-24 '''

import json
import nltk
import os.path
import sys
import xml.etree.ElementTree as ET

# check if arguments have been provided
if not len(sys.argv) > 1:
	print("Provide at least one file, bitte", file=sys.stderr)
	sys.exit()

for file_path in sys.argv[1:]:
	# check if argument is a valid file
	if not os.path.isfile(file_path):
		print("Not a valid file, gtfo", file=sys.stderr)
		sys.exit()

	tree = ET.parse(file_path)

	# enlist the collection of tags
	elem_set = set()
	for elem in tree.iter():
		elem_set.add(elem.tag)
	#print(sorted(list(elem_set)), file=sys.stderr)

	# journal title
	res = tree.findall(".//journal-title")
	if res:
		journal_title = res[0].text
	# journal issn
	res = tree.findall(".//issn")
	if res:
		journal_issn = res[0].text

	# article title
	res = tree.findall(".//article-title")
	if res:
		article_title = res[0].text

	# authors
	res = tree.findall(".//*[@contrib-type='author']/name")
	if res:
		authors = []
		for author in res:
			surname = author.find("surname").text
			given_names = author.find("given-names").text
			authors.append((surname, given_names))

	res = tree.findall(".//article-id[@pub-id-type='pmid']")
	if res:
		pmid = res[0].text

	# abstract
	res = tree.findall(".//abstract/p")
	if res:
		abstract = " ".join(map(lambda x: x.text, res))

	# abstract sentences
	abstract_sentences = nltk.sent_tokenize(abstract)

	# put results into a dict
	document = {
		"pmid" : pmid,
		"article_title" : article_title,
		"authors" : authors,
		"journal_title" : journal_title,
		"journal_issn" : journal_issn,
		"abstract" : abstract,
		"abstract_sentences" : abstract_sentences
	}

	# output results to stdout
	document_string = json.dumps(document, indent=4)
	print(document_string, file=sys.stdout)
