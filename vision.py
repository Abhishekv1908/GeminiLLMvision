from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Directly set the API key (replace with your actual key)
API_KEY = "Google_API_Key"

# Configure the API key
genai.configure(api_key=API_KEY)

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-1.5-pro")

def get_gemini_response(input,image):
    if input!="":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)  # Assign the response  # Assign the response
    return response.text  # Return the actual text


# Initialize Streamlit app
st.set_page_config(page_title="Gemini Image demo By Abhishek")
st.header("Gemini Image demo By Abhishek")
input=st.text_input("Input Prompt:",key="input")

# File uploader
uploaded_file = st.file_uploader("Choose a file", type=[ "png", "jpg", "jpeg"]) 
image=""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="Upload Image.", use_column_width=True)
submit=st.button("Tell me about the image")

# if submitted is clicked
if submit:
    response=get_gemini_response(input,image)
    st.subheader("The response is")
    st.write(response)

