# Use a smaller base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir pytest

# Define the command to run the app
ENTRYPOINT ["python", "app.py"]
