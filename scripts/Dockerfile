# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /cinfo_viewer

# Copy the current directory contents into the container at /app
COPY . /cinfo_viewer

# Install any needed packages specified in requirements.txt
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/streamlit/streamlit-example.git .

RUN pip3 install -r requirements.txt

# Make port 8501 available to the world outside this container
EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Run app.py when the container launches
# CMD ["streamlit", "run", "cinfo_viewer.py"]
ENTRYPOINT ["streamlit", "run", "cinfo_viewer.py", "--server.port=8501", "--server.address=0.0.0.0"]
