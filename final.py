from apps import empty
import streamlit as st
from multiapp import MultiApp
from apps import  Covid,x_ray,empty,tuberculosis,copd# import your app modules here

app = MultiApp()

st.title("Welcome to Lung Disease Prediction Website")
st.write("""The change in the environment,pollution and some unwanted daily habits such as smoking,drinking,etc., can lead to many lung diseases.For detecting the disease and the level of it with the help of patient symptoms or with X-Ray images.So, that the patient can cross check the results.""")

choice_mode=st.selectbox("select_options",("Select","Symptoms","Radiology Images"))

if choice_mode=='Symptoms':
    app.add_app("Select", empty.app)
    app.add_app("Covid Prediction", Covid.app)
    app.add_app("Tuberculosis",tuberculosis.app)
    app.add_app("COPD",copd.app)
    app.run()
elif(choice_mode=='Radiology Images'):
    app.add_app("Upload X-ray image",x_ray.app)
    app.run()