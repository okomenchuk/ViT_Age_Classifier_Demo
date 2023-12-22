# Import necessary libraries and modules
import os                # Provides access to operating system functions
import requests          # Allows sending HTTP requests to external APIs
from fastapi import FastAPI, File, UploadFile  # Imports classes and functions from FastAPI framework
from dotenv import load_dotenv  # Loads environment variables from a .env file

# Load environment variables from a .env file in the project directory
load_dotenv()

# Create an instance of the FastAPI framework
app = FastAPI()

# Retrieve the external API URL from the environment variables
API_URL = os.getenv("API_URL")

# Define a FastAPI route to handle POST requests at "/predict/"
@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Read the content of the uploaded file asynchronously
    content = await file.read()

    # Define headers for the HTTP request with the authentication token
    headers = {"Authorization": f"Bearer {os.getenv('TOKEN')}"}

    # Send an HTTP POST request to the external API with the uploaded file content
    response = requests.post(API_URL, headers=headers, data=content)

    # Parse and extract the response data from the external API as JSON
    result = response.json()

    # Return the result obtained from the external API as the HTTP response
    return result
