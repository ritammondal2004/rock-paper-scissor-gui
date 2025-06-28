# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies including Tkinter
RUN apt-get update && apt-get install -y \
    python3-tk \
    python3-dev \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*
# Copy requirement file and install dependencies
COPY requirements_dev.txt .
RUN pip install --no-cache-dir -r requirements_dev.txt

# Copy rest of the project files
COPY . .

# Set environment variable for display (to avoid tkinter crash in Docker)
ENV DISPLAY=:0 

# Command to run your app
CMD ["python", "rock_paper_scissor.py"]





