# Use official Python 3.12 image
FROM python:3.12-slim

# Install OpenCV and dependencies
RUN apt-get update && apt-get install -y python3-opencv libgl1-mesa-glx

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose the default port for Streamlit
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.headless", "true"]
