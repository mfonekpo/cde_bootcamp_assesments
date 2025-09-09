#!/bin/bash
echo "ETL Process initialized..."


echo "Extraction Phase Started"
# read env file to extract url

source .env # Load environment file into the terminal
# download the csv file into raw directory as instructed

echo "Creating download directory 'raw'"
mkdir -p raw # create the raw directory
echo "Downloading datafile from url:"

wget -qO raw/survey.csv $url # use wget with -qO flag to download file into raw directory quietly
# I used the -q flag to hide the url being logged to the terminal for privacy..
echo "Download complete."
echo "Extraction phase completed. survey.csv data file saved to directory"


if [ -f "raw/survey.csv" ]; then
    echo "File exists"
    echo "Begin Transformation Phase"
else
    echo "File does not exist"
fi

echo "Tranformation Phase Started"
# rename the first column to 'id'
sed -i '1s/Variable_code/variable_code/' raw/survey.csv
echo "columns renamed from 'Variable_code' to 'variable_code'"

# create the transformed directory
mkdir -p Transformed

# select only the following columns: year, Value, Units, variable_code and save it to the transformed directory
awk -F',' '{print $1 "," $9 "," $5 "," $6}' raw/survey.csv > Transformed/2023_year_finance.csv


if [ -f "Transformed/2023_year_finance.csv" ]; then
    echo "File exists"
    echo "Begin Loading Phase"
else
    echo "File does not exist"
fi

echo "Loading phase Started"
# create the gold directory
mkdir -p Gold

# move the transformed file to the gold directory
cp Transformed/2023_year_finance.csv Gold/2023_year_finance.csv

if [ -f "Gold/2023_year_finance.csv" ]; then
    echo "File exists"
    echo "ETL Process completed."
else
    echo "File does not exist"
fi