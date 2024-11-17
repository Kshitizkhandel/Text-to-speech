# Use an official lightweight Python image
FROM python:3.10-slim

# Set a working directory in the container
WORKDIR /app

# Copy the local application code to the container
COPY . .

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    libsndfile1 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir torch coqui-tts

# Define the entry point
ENTRYPOINT ["python", "run_tts.py"]