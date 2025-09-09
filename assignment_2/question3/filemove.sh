#!/bin/bash
echo "File move process initialized..."

# create the json_and_csv directory
mkdir -p json_and_CSV

# move the files to the json_and_csv directory using a wildcard
echo "moving file to designated location..."
mv datafiles/*.{json,csv} json_and_CSV/
echo "File move process completed."