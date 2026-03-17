import streamlit as st
import requests
from PIL import Image

API_URL = "https://ai-image-classifier-web-app-fastapi-an8f.onrender.com"

st.title("AI Image Classifier")
uploaded_file = st.file_uploader("Upload an image",type=['jpg','png','jpeg'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image", use_column_width=True)
    if st.button("predict"):
        files = {"file": uploaded_file.getvalue()}
        response = requests.post(API_URL,files = files)
        if response.status_code == 200:
            result = response.json()
            prediction = result['prediction']
            confidence = result['confidence']
            
            st.subheader("Prediction Result")
            
            st.write(f"Label: **{prediction}**")
            st.write(f"Confidence: **{confidence:.2f}**")
            
        else:
            st.error("API Error")
