#!/bin/sh

# Solr admin URL inside Platform.sh
SOLR_URL="http://solr.internal:8983/solr"

# Check if core exists; if not, create it
if ! curl -s "$SOLR_URL/admin/cores?action=STATUS&core=mycore" | grep -q '"mycore"'; then
  curl "$SOLR_URL/admin/cores?action=CREATE&name=mycore&instanceDir=mycore"
fi
