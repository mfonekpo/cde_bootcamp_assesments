# Use official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY etl/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the ETL code and data
COPY etl/ /app/etl/
COPY data/ /app/data/

# Set entrypoint to run the main ETL script
CMD ["python", "etl/main.py"]