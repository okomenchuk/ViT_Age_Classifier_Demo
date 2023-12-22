# Use the base image "tiangolo/uvicorn-gunicorn:python3.9-slim" with Python 3.9
FROM tiangolo/uvicorn-gunicorn:python3.9-slim

# Define a build argument "WORK_DIR" with a default value of "/app"
ARG WORK_DIR="/app"

# Set the working directory inside the container to the value of the "WORK_DIR" argument
WORKDIR ${WORK_DIR}

# Copy the "requirements.txt" file from the local directory to the container's working directory
COPY requirements.txt ${WORK_DIR}

# Install or upgrade pip, install Python packages listed in "requirements.txt," and purge the pip cache
RUN pip install -U pip && \
    pip install --no-cache-dir -r ${WORK_DIR}/requirements.txt && \
    pip cache purge

# Copy the "app.py" and ".env" files from the local directory to the container's working directory
COPY app.py ${WORK_DIR}
COPY .env ${WORK_DIR}

# Expose port 8000, which is the port where the FastAPI application will run
EXPOSE 8000

# Define the command to run when the container is started
CMD [ "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload" ]
