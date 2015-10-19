from __future__ import print_function

""" This program preprocesses XML files from PubMed Central and extracts the
relevant information (authors, title, abstract text, sentences, etc). The
output should be ready to be processed by an NLP pipeline in a lightweight
format (such as JSON?).

Usage: 

	preprocess.py <some_file>.xml [<another_file>.xml ...]
	
	or
	
	find . | grep xml | python preprocess.py"""

from functools import reduce
import itertools
import json
import os.path
import sys
import xml.etree.ElementTree as ET

# delimiter used to separate JSON documents without blocking
DELIMITER = "---"

# check if arguments have been provided
if len(sys.argv) > 1:
	file_paths = sys.argv[1:]
# if not, read filenames from stdin
else:
	file_paths = sys.stdin.readlines()

# flag used to avoid printing the delimiter the first time
first_document = True 

for file_path in file_paths:
	file_path = file_path.strip()
	
	# output delimiter to stdin to signal end of document
	if not first_document:
		print(DELIMITER, file=sys.stdout)
	
	# set the flag to False
	first_document = False

	# check if argument is a valid file
	if not os.path.isfile(file_path):
		raise IOError("file not found, gtfo")

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
		abstract = " ".join(reduce(lambda x, y: itertools.chain(x, y), \
			map(lambda x: x.itertext(), res)))

	# put results into a dict
	document = {
		"pmid" : pmid,
		"article_title" : article_title,
		"authors" : authors,
		"journal_title" : journal_title,
		"journal_issn" : journal_issn,
		"abstract" : abstract
	}

	# output results to stdout
	print(json.dumps(document, indent=4), file=sys.stdout)
