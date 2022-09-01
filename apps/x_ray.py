import streamlit as st
from PIL import Image,ImageOps
import tensorflow as tf
from tensorflow import keras 
from keras.models import load_model
import cv2
import numpy as np

def app():

    file = st.file_uploader("Upload Image")
    if file!=None:
        img = Image.open(file)

        model = load_model("G:\Jupyter notebooks\CovidModelEfficientNet.h5")
        model.compile(loss='binary_crossentropy',
                    optimizer='rmsprop',
                    metrics=['accuracy'])
        size=(224,224)
        img = ImageOps.fit(img,size,Image.ANTIALIAS)
        img = np.asfarray(img)
        img = cv2.resize(img,(224,224))
        img = np.reshape(img,[1,224,224,1])
        

        classes = model.predict(img)
        st.write(classes)
        maxi=np.argmax(classes)
        if(maxi==0):
            st.success("Disease: COVID")
        elif(maxi==2):
            st.success("Disease: PNEUMONIA")
        elif(maxi==3):
            st.success("Disease: TUBERCULOSIS")
        else:
            st.success("No Disease")
    else:
        st.write("Select an image")