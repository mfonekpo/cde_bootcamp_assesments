#!/bin/bash
set -e  # stop script if any command fails

# Define your network name
NETWORK_NAME="etl_network"

# Check if network already exists
if ! docker network ls | grep -q "$NETWORK_NAME"; then
  echo "🔌 Creating Docker network: $NETWORK_NAME"
  docker network create "$NETWORK_NAME"
else
  echo "✅ Docker network $NETWORK_NAME already exists"
fi

# Export as an environment variable so docker-compose can use it
export NETWORK_NAME

# Run docker-compose with this network
docker compose up -d --build
