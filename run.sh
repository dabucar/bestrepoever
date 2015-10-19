#
# This script sets up environment variables and runs the pipelne.
#
# Usage: ./run.sh [<target_folder> [<python_command>]]
# Example:
#   To run the pipeline on the 2 sample data files:
#     ./run sample
#   Gangsta mode: run the pipeline on the data (after running ./fetch_data.sh):
#     ./run data
#
# Where <target_folder> is the folder where the xml files are found. If this is
# not specified, "sample" is assumed. <python_command> is an optional parameter
# in case the python command is not 'python' (for example 'python2.7').
#
# For debugging purposes, sterr is written to an "error.log" file.
#

export PYTHONPATH=utils:$PYTHONPATH

if [ $# -lt 1 ]
	then
		TARGET_FOLDER=sample
	else
		TARGET_FOLDER=$1
fi
if [ $# -lt 2 ]
	then
		PYTHON_COMMAND=python
	else
		PYTHON_COMMAND=$2
fi

find $TARGET_FOLDER | grep xml | $PYTHON_COMMAND tools/preprocess.py | \
	$PYTHON_COMMAND tools/sentence_detect.py abstract article_title 2> error.log
