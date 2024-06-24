#!/bin/bash 
 
# Navigate to the directory of the script 
SCRIPT_DIR=$(dirname $0) 
echo $SCRIPT_DIR 
 
# Install the required Python package 
python3 -m pip install requests --quiet 
 
# Change to the scripts directory 
cd $SCRIPT_DIR/scripts/ 
 
# Run the modified Python script and output to a single m3u file 
python3 YouTube_Live.py > ../YouTube_Live.m3u 
 
echo "m3u file generated"
