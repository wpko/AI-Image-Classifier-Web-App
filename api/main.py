from fastapi import FastAPI, UploadFile, File
import tensorflow as tf
import numpy as np
from PIL import Image
import io

app = FastAPI()

model = tf.keras.models.load_model("model/image_model.h5", compile=False)

IMG_SIZE = (224,224)

def preprocess_image(image):
    image = image.resize(IMG_SIZE)
    image = np.array(image)/255.0
    image = np.expand_dims(image,axis=0)
    
    return image

@app.get('/')
def home():
    return{"message": "AI Image Classifier API running"}

@app.post('/predict')
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")
    img = preprocess_image(image)
    prediction = model.predict(img)[0][0]
    
    if prediction > 0.5:
        label = "Dog"
    else:
        label = "Cat"
        
    return {
        "prediction": label,
        "confidence": float(prediction)
    }
