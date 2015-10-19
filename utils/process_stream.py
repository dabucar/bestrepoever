""" This function reads input from stdin and stores lines into a buffer until
a predefined delimiter line is found. When the delimiting line is found, the
buffer (an individual JSON file) is parsed into a Python dictionary (a document)
and it's passed as parameter to the given function.

Usage: processStream(<some_function>)""" 

from __future__ import print_function
import json, sys, traceback

DELIMITER = "---" + "\n"

def processStream(processDocument):
	# Read from stdin
	buffer = ""
	while True:
		line = sys.stdin.readline()
		# If line is a delimiter, process the JSON document in buffer and flush
		# the buffer. Else, add line to the buffer.
		if line == DELIMITER:
			document = json.loads(buffer)
			try:
				processed_document = processDocument(dict(document))
				print(json.dumps(processed_document, indent=4), file=sys.stdout)
			except Exception:
				print(traceback.format_exc(), file=sys.stderr)
			buffer = ""
		else:
			buffer += line
	# Process the last remaining buffer.
	document = json.loads(buffer)
	processed_document = processDocument(dict(document))
	print(json.dumps(processed_document, indent=4), file=sys.stdout)
