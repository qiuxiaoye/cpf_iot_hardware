# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install Paho MQTT client
RUN pip install paho-mqtt

# Command to run when the container starts
CMD ["python", "./paho_mqtt.py"]
