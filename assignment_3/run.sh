#!/bin/bash

# Set variables
NETWORK_NAME="etl_net"
DB_CONTAINER_NAME="db"
ETL_IMAGE_NAME="etl"
DB_USER="etl_user"
DB_PASSWORD="etl_pass"
DB_NAME="etl_db"

# Step 1: Create Docker network
echo "Creating Docker network: $NETWORK_NAME"
docker network create $NETWORK_NAME

# Step 2: Start PostgreSQL container
echo "Starting PostgreSQL container: $DB_CONTAINER_NAME"
docker run -d \
  --name $DB_CONTAINER_NAME \
  --network $NETWORK_NAME \
  -e POSTGRES_USER=$DB_USER \
  -e POSTGRES_PASSWORD=$DB_PASSWORD \
  -e POSTGRES_DB=$DB_NAME \
  postgres:14

# Step 3: Wait for DB to be ready
echo "Waiting for PostgreSQL to be ready..."
until docker exec $DB_CONTAINER_NAME pg_isready -U $DB_USER -d $DB_NAME; do
  sleep 2
done
echo "PostgreSQL is ready!"

# Step 4: Build ETL Docker image
echo "Building ETL Docker image: $ETL_IMAGE_NAME"
docker build -t $ETL_IMAGE_NAME .

# Step 5: Run ETL container and execute pipeline
echo "Running ETL pipeline..."
docker run --rm \
  --network $NETWORK_NAME \
  -e DB_HOST=$DB_CONTAINER_NAME \
  -e DB_PORT=5432 \
  -e DB_USER=$DB_USER \
  -e DB_PASSWORD=$DB_PASSWORD \
  -e DB_NAME=$DB_NAME \
  $ETL_IMAGE_NAME

echo "ETL pipeline completed!"

# Step 6: Cleanup (comment out if you want to inspect)
echo "Cleaning up..."
docker stop $DB_CONTAINER_NAME
docker rm $DB_CONTAINER_NAME
docker network rm $NETWORK_NAME