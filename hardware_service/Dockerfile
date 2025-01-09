# Use a minimal Python base image for ARM
FROM python:3.9-slim-bullseye

# Set the working directory
WORKDIR /app

# This is only needed for raspberry pi
# Install necessary system dependencies for building Python packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    build-essential \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy only necessary files
COPY . /app/
COPY requirements.txt /app/

# COPY app.py /app/
# COPY requirements.txt /app/
# COPY configuration /app/configuration
# COPY database /app/database
# COPY utils /app/utils


# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port for Flask
EXPOSE 5001

# Run the application
CMD ["python", "app.py"]