import streamlit as st
from tensorflow.keras.models import load_model
import os
import numpy as np
from PIL import Image

#model path
try:
    model_path=r'C:\Users\visha\jupyter\pycharm\pythonProject\emoticon_model.keras'
    new_model=load_model(model_path)
except:
    st.error("Refresh")

#classes
classes=['anger','fear','disgust','happy','neutral','sad','surprise']

def imageToArray(imageName):
  # Load the image and resize it to the desired dimensions
  image_path = f'{imageName}.jpg'
  width, height = 48,48  # Replace with the dimensions required by your model

  image = Image.open(imageName)
  image = image.resize((width, height))
  print(image.width)
  # Convert the image to a NumPy array and normalize the pixel values (if necessary)
  image_array = np.asarray(image)
  image_array = image_array / 255.0  # Normalize the pixel values between 0 and 1

  print(image_array.shape)
  # Reshape the image array to match the input shape of your model
  image_array = image_array.reshape(1, width, height, 3)  # Assumes the input shape is (width, height, 3)

  return image_array


#streamlit
st.title("Predict Emotions")



uploaded_files = st.file_uploader("Choose an image file !",type="jpg",accept_multiple_files=True)

if uploaded_files is not None and len(uploaded_files)>0:
    for uploaded_file in uploaded_files:
        with st.container(border=True):
            st.image(uploaded_file)
            img=imageToArray(uploaded_file)
            pred = new_model.predict(img)
            preds_single = classes[np.argmax(pred)]
            st.header("Emotion : "+preds_single)
            st.subheader("Confidence : "+str((round(np.max(pred)*100,2)))+"%")
