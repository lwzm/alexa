#!/bin/sh
set -e
cd top-1m.csv.zip.d/
fn=$(date '+%G%m%d')
curl --socks5 localhost http://s3.amazonaws.com/alexa-static/top-1m.csv.zip >zip/$fn
unzip zip/$fn
mv top-1m.csv csv/$fn
cut -d , -f 2 csv/$fn >hosts/$fn

exit

grep -E '^[0-9]+.,8090lu\.com$' csv/*
grep -m 1 -n -E '^git\.com$' hosts/*
