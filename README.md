# AI Image Classifier Web App

![Python](https://img.shields.io/badge/Python-3.10-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep%20Learning-orange)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Computer Vision](https://img.shields.io/badge/Computer%20Vision-CNN-purple)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Image%20Classification-red)
![Status](https://img.shields.io/badge/Project-Portfolio-blueviolet)

An **AI-powered Image Classification Web Application** that predicts image categories using a **Convolutional Neural Network (CNN)**.

This project demonstrates a **complete Computer Vision Machine Learning pipeline** including:

- Image preprocessing
- CNN model training
- Model evaluation
- FastAPI deployment
- Image prediction API

---

# Project Overview

This application allows users to upload an image and receive predictions from a trained deep learning model.

The CNN model is built using **TensorFlow / Keras** and integrated into a **FastAPI backend** for real-time image inference.

This project demonstrates how **AI models can be integrated into real-world applications**.

---

# Model Performance

| Metric | Value |
|------|------|
| Training Accuracy | 91% |
| Validation Accuracy | 79% |
| Training Loss | 0.22 |
| Validation Loss | 0.50 |

The model shows good performance with acceptable generalization.

---

# Training Visualization

The following graph shows the training results of the CNN model.

![Training Results](assets/training_results.png)

The graph includes:

- Training Accuracy
- Validation Accuracy
- Training Loss
- Validation Loss

---

# Features

- CNN-based image classification
- Image preprocessing and normalization
- Data augmentation for improved model performance
- FastAPI backend prediction API
- Model training visualization
- Modular project structure

---

# Tech Stack

### Programming Language
- Python

### Deep Learning
- TensorFlow
- Keras

### Backend
- FastAPI

### Data Processing
- NumPy
- Pillow

### Visualization
- Matplotlib

---

# System Architecture


User Image
↓
FastAPI API
↓
Image Preprocessing
↓
CNN Model
↓
Prediction Result


---

# Project Structure


ai-image-classifier-web-app

api
└── main.py

model
└── image_model.h5

dataset
├── train
└── test

assets
└── training_results.png

requirements.txt
README.md


---

# Installation

Clone the repository


git clone https://github.com/your-username/ai-image-classifier.git


Navigate to project folder


cd ai-image-classifier


Install dependencies


pip install -r requirements.txt


---

# Train the Model

Run the training script


python train_model.py


The trained model will be saved as


model/image_model.h5


---

# Run FastAPI Server

Start the API server


uvicorn api.main:app --reload


API will run at


http://127.0.0.1:8000


API documentation


http://127.0.0.1:8000/docs


---

# API Example

### POST Request


POST /predict


Upload an image file and the API will return the predicted class.

Example Response

```json
{
  "prediction": "Cat",
  "confidence": 0.94
}```
Future Improvements

Improve model accuracy using larger datasets

Add multi-class classification

Build a web frontend interface

Deploy the application to cloud platforms

Add model monitoring

Author

Wai Lay

Aspiring Python / AI Developer

GitHub
https://github.com/wpko
