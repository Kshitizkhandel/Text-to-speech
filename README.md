# Coqui-TTS with Docker  

This guide explains how to use Coqui-TTS with Docker to synthesize text-to-speech audio.  

## Prerequisites  

- Docker installed on your machine.  
- A sample voice file (e.g., `example_voice.flac`).  

## Usage  

### Build and Run the Docker Image  

Build the Docker image using the provided `Dockerfile`.  

```bash  
docker build -t <image_name> .  

sudo docker run -v $(pwd)/output:/app/output -v $(pwd)/ref.wav:/app/ref.wav <image_name> --text "Hello, this is a test message" --reference_voice /app/ref.wav--output "/app/output/test.wav" 
