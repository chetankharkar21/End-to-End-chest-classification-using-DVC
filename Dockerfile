# Use an official Python runtime as a base image with Python 3.11
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update -y && apt-get install -y \
    awscli \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    gcc

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt to the /app directory inside the container
COPY End-to-End-chest-classification-using-DVC/requirements.txt /app/requirements.txt

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the rest of the application
COPY . /app

# Clean up to reduce image size
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Run the application when the container starts
CMD ["python", "app.py"]
