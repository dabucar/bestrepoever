from __future__ import print_function

''' ain't nobody got time fo wait '''
''' XML extraction v0.0.0.0.1 '''
''' dabucar 2015-08-24 '''

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
    print(sorted(list(elem_set)), file=sys.stderr)

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

    print(journal_title, journal_issn, article_title, authors)

