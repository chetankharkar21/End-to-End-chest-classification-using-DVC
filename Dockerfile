# Use an official Python runtime as a base image with Python 3.11
FROM python:3.11-slim

# Set the working directory in the container
RUN apt update -y && apt install awscli -y
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app
RUN pip install -r requirements.txt

# Run the application when the container starts
CMD ["python", "app.py"]
