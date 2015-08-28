''' ain't nobody got time fo wait '''
''' XML extraction v0.0.0.0.1 '''
''' dabucar 2015-08-24 '''

import os.path
import sys
import xml.etree.ElementTree as ET

# check if argument provided
if not len(sys.argv) > 1:
	print "Provide a file, bitte"
	sys.exit()

# check if argument is a valid file
file_path = sys.argv[1]
if not os.path.isfile(file_path):
	print "Not a valid file, gtfo"
	sys.exit()

tree = ET.parse(file_path)

# enlist the collection of tags
elem_set = set()
for elem in tree.iter():
	elem_set.add(elem.tag)
print sorted(list(elem_set))

# journal title
res = tree.findall(".//journal-title")
if not res is None:
	journal_title = res[0].text 
# journal issn
res = tree.findall(".//issn")
if not res is None:
	journal_issn = res[0].text 

# article title
res = tree.findall(".//article-title")
if not res is None:
	article_title = res[0].text 

# authors
res = tree.findall(".//*[@contrib-type='author']/name")
if not res is None:
	authors = []
	for author in res:
		surname = author.find("surname").text
		given_names = author.find("given-names").text
		authors.append((surname, given_names))

print journal_title, journal_issn, article_title, authors

