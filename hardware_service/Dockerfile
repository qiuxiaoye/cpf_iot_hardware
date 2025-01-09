# Use a minimal Python base image for ARM
FROM python:3.9-slim-bullseye

# Set the working directory
WORKDIR /app

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