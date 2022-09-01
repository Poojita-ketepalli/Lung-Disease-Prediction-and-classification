import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
def app():
    data = pd.read_csv(r"D:\6th sem\CSP\Website\apps\Covid Prediction.csv",dtype=str)

    def user_input():
        Cough = st.sidebar.selectbox("Cough",("Yes","No","None"))
        Fever = st.sidebar.selectbox("Fever",("Yes","No","None"))
        Sore_Throat = st.sidebar.selectbox("Sore_Throat",("Yes","No","None"))
        Shortness_of_Breath = st.sidebar.selectbox("Shortness_of_Breath",("Yes","No",None))
        Headache = st.sidebar.selectbox("Headache",("Yes","No","None"))
        Age_60_or_above = st.sidebar.selectbox("Age_60_or_above",("Yes","No","None"))
        Gender = st.sidebar.selectbox("Gender",("female","male","None"))
        Test_Indication = st.sidebar.selectbox("Test_Indication",("Contact with confirmed","Abroad","Other"))
        data = {
            'Cough':Cough,
            'Fever':Fever,
            'Sore Throat':Sore_Throat,
            'Shortness of Breath':Shortness_of_Breath,
            'Headache':Headache,
            'Age 60 or above':Age_60_or_above,
            'Gender':Gender,
            'Test Indication':Test_Indication
        }
        features = pd.DataFrame(data,index=[1],dtype=str)
        return features
    df = user_input()
    st.subheader("User Input Parameters")
    st.write(df)

    num1={'0':0,'1':1,'None':2}
    num2={'negative':0,'positive':1,'other':2}
    num3={'No':0,'Yes':1,'None':2}
    num4={'female':0,'male':1,'None':2}
    num5={'Contact with confirmed':0,'Abroad':1,'Other':2}

    

    data["cough"]=data["cough"].map(num1)
    data["fever"]=data["fever"].map(num1)
    data["sore_throat"]=data["sore_throat"].map(num1)
    data["shortness_of_breath"]=data["shortness_of_breath"].map(num1)
    data["head_ache"]=data["head_ache"].map(num1)
    data["corona_result"]=data["corona_result"].map(num2)
    data["age_60_and_above"]=data["age_60_and_above"].map(num3)
    data["gender"]=data["gender"].map(num4)
    data["test_indication"]=data["test_indication"].map(num5)

    df["Cough"]=df["Cough"].map(num3)
    df["Fever"]=df["Fever"].map(num3)
    df["Sore Throat"]=df["Sore Throat"].map(num3)
    df["Shortness of Breath"]=df["Shortness of Breath"].map(num3)
    df["Headache"]=df["Headache"].map(num3)
    df["Age 60 or above"]=df["Age 60 or above"].map(num3)
    df["Gender"]=df["Gender"].map(num4)
    df["Test Indication"]=df["Test Indication"].map(num5)

    data.drop('test_date',axis=1,inplace=True)
    data = data[data['corona_result']!=2]

    x=data.drop('corona_result',axis=1)
    y=data['corona_result']

    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=1)

    tree = DecisionTreeClassifier()
    tree.fit(x_train,y_train)
    y_pred_dt = tree.predict(x_test)
    confusion_matrix(y_test,y_pred_dt)
    accuracy = accuracy_score(y_test,y_pred_dt)
    output = tree.predict(df)
    st.write("# Prediction")

    if output==0:
        value="Negative"
    elif output==1:
        value="Positive"

    def predict():
        st.success("Result: "+value)

    st.button("Predict",on_click=predict)
    st.write("Scroll to top of page to see the result after clicking on predict!!!")

