# Use the base image "python:3.9-slim" with Python 3.9
FROM python:3.9-slim

# Define a build argument "WORK_DIR" with a default value of "/ui"
ARG WORK_DIR="/ui"

# Set the working directory inside the container to the value of the "WORK_DIR" argument
WORKDIR ${WORK_DIR}

# Copy the "requirements.txt" file from the local directory to the container's working directory
COPY requirements.txt ${WORK_DIR}

# Install or upgrade pip, install Python packages listed in "requirements.txt," and purge the pip cache
RUN pip install -U pip && \
    pip install --no-cache-dir -r ${WORK_DIR}/requirements.txt && \
    pip cache purge

# Copy the "ui.py" and ".env" files from the local directory to the container's working directory
COPY ui.py ${WORK_DIR}
COPY .env ${WORK_DIR}

# Expose port 8501, which is the default port for Streamlit applications
EXPOSE 8501

# Define the command to run when the container is started
CMD [ "streamlit", "run", "ui.py" ]
