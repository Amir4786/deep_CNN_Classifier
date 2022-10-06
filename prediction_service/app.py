import streamlit as st
import pandas as pd 
import tensorflow as tf
import numpy as np
from PIL import Image

'''
Deep Classifier Project 
'''
model= tf.keras.models.load_model("model.h5")
uploaded_file= st.file_uploader("Choose a file")
if uploaded_file is not None:
    image= Image.open(uploaded_file)
    img= image.resize((224,224))
    img_array= np.array(img)
    img_array= np.expand_dims(img_array, axis=0) # [batch_size, row, column, channel]
    result= model.predict(img_array)

if argmax_index[0]==0:
    st.image(image, caption="Predicted: Cat")
else:
    st.image(image, caption="Predicted: Dog")
