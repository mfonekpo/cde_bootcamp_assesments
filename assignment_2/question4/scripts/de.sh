#!/bin/bash
# Bash script to copy CSV files into a PostgreSQL database

source .env # Load environment file into the terminal

# Database connection details

DB_NAME=$DB_NAME
DB_USER=$DB_USER
DB_HOST=$DB_HOST
DB_PORT=$DB_PORT
CSV_DIR="./datafiles"

export PGPASSWORD=$DB_PASSWORD

for file in "$CSV_DIR"/*.csv; do
    table_name=$(basename "$file" .csv)
    echo "Loading $file into table: $table_name"

    # Extract header row
    header=$(head -n 1 "$file")

    # Convert header into SQL column definitions (all TEXT type for now)
    columns=$(echo "$header" | awk -F',' '{for(i=1;i<=NF;i++) printf "%s TEXT%s", $i, (i<NF?", ":"") }')

    # Drop and recreate table
    psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME -c "DROP TABLE IF EXISTS $table_name;"
    psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME -c "CREATE TABLE $table_name ($columns);"

    # Import CSV
    psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME -c "\copy $table_name FROM '$file' CSV HEADER;"
done
