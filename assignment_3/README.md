# Docker Assignment: Python ETL Pipeline with Dockerized Database
- Dockerize a Python ETL pipeline.
- Create a Docker database container that runs isolated with the ETL container.
- Use Docker networking to connect the ETL pipeline and database containers.
- Write Python scripts to demonstrate:
    - Extraction
    - Transformation
    - Loading
- Create a bash script that:
    - Starts the Docker containers
    - Creates the necessary connections
    - Runs the full ETL pipeline in a detailed automated way
- Submit a GitHub repository containing:
    - All code (ETL scripts, Dockerfiles, bash script)
    - A detailed README file with step-by-step instructions on running the pipeline.
- Submission deadline: before next class on Wednesday.




# Dockerized Python ETL Pipeline

This repository contains a Dockerized Python ETL (Extract, Transform, Load) pipeline. It demonstrates:
- Extracting data from a sample CSV file.
- Transforming the data (cleaning and formatting).
- Loading the transformed data into a PostgreSQL database.
- Running the ETL in a Docker container connected to an isolated PostgreSQL Docker container via Docker networking.

## Prerequisites
- Docker installed on your system.
- Basic knowledge of Docker and Python.

## Directory Structure
- `Dockerfile`: Builds the ETL container.
- `run.sh`: Bash script to start containers, create network, and run the ETL.
- `data/sample.csv`: Sample input data for extraction.
- `etl/`: Contains Python scripts for the ETL pipeline.
  - `extract.py`: Handles data extraction.
  - `transform.py`: Handles data transformation.
  - `load.py`: Handles data loading into the DB.
  - `main.py`: Orchestrates the full ETL process.
  - `requirements.txt`: Python dependencies.

## Step-by-Step Instructions to Run the Pipeline

1. **Clone the Repository**
2. `cd` into assignement_3 directory
3. **Make the Bash Script Executable** (if on Unix-like system): `chmod +x run.sh`
4. **Run the Bash Script**:
   ```bash
   ./run.sh
   ```
This script will:
- Create a Docker network (`etl_net`).
- Start the PostgreSQL container (`db`) on the network.
- Wait for the DB to be ready.
- Build the ETL Docker image (`etl`).
- Run the ETL container on the same network, executing the pipeline.
- Clean up containers and network after completion (optional; comment out if you want to inspect).

Example output:
- The script logs progress.
- ETL logs show extraction, transformation, and loading steps.
- Data is loaded into the `users` table in the `etl_db` database.

4. **Inspect the Database (Optional)**:
If you want to verify the loaded data without cleaning up:
- Comment out the cleanup lines in `run.sh`.
- After running, connect to the DB container: `docker exec -it db psql -U etl_user -d etl_db`
- Run SQL queries to inspect the `users` table. `SELECT * FROM users;`

------------
- Exit with `\q`.

## ETL Details
- **Extraction**: Reads `data/sample.csv` (columns: name, age, email).
- **Transformation**: Converts age to int, uppercases name, validates email (dummy check).
- **Loading**: Connects to PostgreSQL (host: `db`, port: 5432) and inserts data into `users` table.
- The DB is initialized with a user (`etl_user`), password (`etl_pass`), and database (`etl_db`).

## Troubleshooting
- Ensure Docker is running.
- If DB connection fails, increase the wait time in `run.sh`.
- For production, use Docker Compose for better orchestration and secure credentials.

## License
MIT License.