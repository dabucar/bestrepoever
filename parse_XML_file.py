''' ain't nobody got time fo wait '''
''' XML extraction v0.0.0.0.1 '''
''' dabucar 2015-08-24 '''

import codecs
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

pmids = tree.findall(".//PubmedArticle/MedlineCitation/PMID")

# journal title
jtitles = tree.findall(".//Article/Journal/Title")

# journal issn
issns = tree.findall(".//Article/Journal/ISSN")

# article title
atitles = tree.findall(".//ArticleTitle")

# abstract
abstracts = tree.findall(".//Article/Abstract")

# authors
alists = tree.findall(".//AuthorList")
lnfnlist = []
for al in alists:
    lnfn = []
    for auth in al.findall("Author"):
        ln, fn = auth.findtext("LastName"), auth.findtext("ForeName")
        lnfn.append(ln+", "+fn)
    lnfnlist.append(lnfn)

utf8 = codecs.getencoder("UTF-8")
for i in range(len(pmids)):
    print utf8("\n" + "".join(pmids[i].itertext()) + "\n" + "".join(jtitles[i].itertext()) + "\n" + "".join(issns[i].itertext()) + "\n" + "".join(atitles[i].itertext()) + "".join(abstracts[i].itertext()) + "\n".join(lnfnlist[i]))[0]

