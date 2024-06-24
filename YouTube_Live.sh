#!/bin/bash

echo $(dirname $0)

python3 -m pip install requests

cd $(dirname $0)/scripts/
 
# Run the modified Python script and output to a single m3u file 
python3 YouTube_Live.py > ../YouTube_Live.m3u 
 
echo "m3u file generated"
