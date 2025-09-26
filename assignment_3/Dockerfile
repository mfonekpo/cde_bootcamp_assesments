FROM python:3.11
WORKDIR /app

COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt



CMD ["python", "./etl/main.py"]
