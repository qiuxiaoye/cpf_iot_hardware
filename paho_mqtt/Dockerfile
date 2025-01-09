# Use an official Python runtime as a parent image
FROM python:3.9-slim-bullseye

# Set the working directory to /app
WORKDIR /app

# Install necessary system dependencies for building Python packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    build-essential \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
# EXPOSE 80

# Define environment variable (optional, can also use .env file as previously discussed)
# ENV COSMOS_DB_CONNECTION_STRING="Your_Cosmos_DB_Connection_String"
# ENV COSMOS_DB_NAME="Your_Database_Name"

# Command to run when the container starts
CMD ["python", "./paho_mqtt.py"]
