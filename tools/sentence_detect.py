""" This program reads input from stdin and stores lines into a buffer until
a predefined delimiter line is found. When the delimiting line is found the
buffer is parsed as JSON, a set of its elements (specified by the user) are
split into sentences and the array of sentences is added to the JSON document.
The resulting JSON document is written to stdout.

Usage: preprocess.py <some_file>.txt | sentence_detect.py <field1> <field2>
Where field1 and field2 are the fields of the JSON documents that need to be
split in sentences."""

from process_stream import processStream
import nltk, sys

arguments = sys.argv[1:]

# Process the document by spliting the given fields into sentences and adding
# them to the document (document is a Python dictionary).
def sentenceDetect(document):
	for field in arguments:
		sentences = nltk.sent_tokenize(document[field])
		document[field + "_sentences"] = sentences
	return document

# main loop
if __name__ == "__main__":
	processStream(sentenceDetect)
