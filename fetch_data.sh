#!/bin/sh

# This script fetches all the data from PubMed and puts it into a 'data' folder.

set -e

mkdir -p data
cd data
wget ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/articles.A-B.tar.gz
wget ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/articles.C-H.tar.gz
wget ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/articles.I-N.tar.gz
wget ftp://ftp.ncbi.nlm.nih.gov/pub/pmc/articles.O-Z.tar.gz
for file in $(ls *tar.gz); do
  tar -xvf $file
done
rm -rf *.tar.gz
