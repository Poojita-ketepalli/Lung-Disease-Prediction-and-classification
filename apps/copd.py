import streamlit as st
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

def app():
    data2 = pd.read_csv(r"D:\6th sem\CSP\Website\lung.csv")

    def user_input():
        Age = st.sidebar.slider("Age",1,100)
        packhistory = st.sidebar.slider("Pack History : person’s pack years smoking, where pack years is defined as twenty cigarettes smoked every day for one year",1,150)
        mwt1 = st.sidebar.slider("MWT1 : Distance that patient walks in 6 minutes in meters (attempt 1)",50,1000)
        mwt2 = st.sidebar.slider("MWT2 : Distance that patient walks in 6 minutes in meters (attempt 2)",50,1000)
        mwtbest = st.sidebar.slider("MWTBest : Distance that patient walks in 6 minutes in meters (best attempt)",50,1000)
        fev1 = st.sidebar.slider("FEV1 : Amount of air you can force from your lungs in one second in litres. Measure of lung function",50,1000)
        data = {
            "Age":Age,
            "Pack History":packhistory,
            "MWT1":mwt1,
            "MWT2":mwt2 ,
            "MWTBest":mwtbest,
            "FEV1":fev1
        }
        features = pd.DataFrame(data,index=[1])
        return features
    df = user_input()
    st.subheader("User Input Parameters")
    st.write(df)

    data2["MWT1"] = data2["MWT1"].fillna(data2["MWT1"].median())
    data2["MWT2"] = data2["MWT2"].fillna(data2["MWT2"].median())
    data2["MWT1Best"] = data2["MWT1Best"].fillna(data2["MWT1Best"].median())

    data2.drop('Unnamed: 0',axis=1,inplace=True)
    data2.drop('ID',axis=1,inplace=True)

    data2=data2.loc[:,:"FEV1"]

    copd_num = {'MILD':0,'MODERATE':1,'SEVERE':2,'VERY SEVERE':3}
    data2['COPDSEVERITY']=data2['COPDSEVERITY'].map(copd_num)

    x = data2.drop("COPDSEVERITY",axis=1)
    x = pd.DataFrame(x,dtype=float)
    y=data2['COPDSEVERITY']

    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=1)
    x_train = x_train.fillna(x_train.mean())

    tree = DecisionTreeClassifier()
    tree.fit(x_train,y_train)
    y_pred_dt = tree.predict(x_test)

    copd_obj = {0:'MILD',1:'MODERATE',2:'SEVERE',3:'VERY SEVERE'}
    ans=tree.predict(df)
    
    def predict():
        result=copd_obj[ans[0]]
        st.success("Result: "+result)

    st.button("Predict",on_click=predict)
    st.write("Scroll to top of page to see the result after clicking on predict!!!")

    

    

