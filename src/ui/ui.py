# Import necessary libraries and modules
import json  # Provides JSON manipulation functions
import os  # Provides access to operating system functions
import requests  # Allows sending HTTP requests to external APIs
import streamlit as st  # Imports the Streamlit library for creating web apps
from PIL import Image  # Imports the Python Imaging Library for image processing
from dotenv import load_dotenv  # Loads environment variables from a .env file

# Load environment variables from a .env file in the project directory
load_dotenv()

# Constants - Retrieve configuration from environment variables
API_URL = os.getenv("API_URL")  # External API URL
PREDICTION_ENDPOINT = os.getenv("PREDICTION_ENDPOINT")  # Endpoint for predictions

# Streamlit configuration
st.set_page_config(layout="wide")  # Set Streamlit app layout
st.markdown('<h1 style="text-align: center; color: #fffff;">ViT Age Classifier</h1>',
            unsafe_allow_html=True)  # Display a centered title in markdown

# Display introductory text
st.write(
    '''
    This is a simple app for the classification of ViT Age Classifier.
    This Streamlit example uses a FastAPI service as the backend.
    Visit this URL at `http://0.0.0.0:8000/docs` for FastAPI documentation.
    '''
)

# File uploader widget
input_image = st.file_uploader('Choose an image', type=['jpg', 'jpeg', 'png'])

# Prediction button
if st.button('Get Prediction'):
    if input_image is not None:
        files = {'file': input_image}

        # Send an HTTP POST request to the external API with the uploaded image
        response = requests.post(API_URL + PREDICTION_ENDPOINT, files=files, timeout=500)

        # Display the uploaded image
        image = Image.open(input_image)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.write('Please wait while predicting...')

        # Parse prediction results if the request is successful (status code 200)
        if response.status_code == 200:
            try:
                predicted_data = json.loads(response.content.decode('utf-8'))

                # Ensure that predicted_data is a list of dictionaries
                if isinstance(predicted_data, list) and all(isinstance(item, dict) for item in predicted_data):
                    # Now you can safely access 'score' within each dictionary
                    scores = [item['score'] for item in predicted_data]
                    st.bar_chart(scores)
                    labels = [item['label'] for item in predicted_data]
                    st.write(labels)
                else:
                    st.write("Invalid data format received from the API.")
            except json.JSONDecodeError:
                st.write("Failed to decode JSON response from the API.")
        else:
            st.write(f'Error: {response.status_code} - Failed to get prediction.')

    else:
        st.write('Insert an image for prediction!')
