#!/bin/bash

# Build the Docker image
docker build -t docx-to-pdf .

# Run the Docker container
docker run -p 5000:5000 docx-to-pdf
