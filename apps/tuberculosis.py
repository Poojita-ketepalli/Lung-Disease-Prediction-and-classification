import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
def app():
    data1 = pd.read_csv(r"D:\6th sem\CSP\Website\apps\Tuberculosis.csv",dtype=str)
    print(data1["gender"].unique())
    print(data1["fever for two weeks"].unique())
    print(data1["coughing blood"].unique())
    print(data1["sputum mixed with blood"].unique())
    print(data1["night sweats "].unique())
    print(data1["chest pain"].unique())
    print(data1["back pain in certain parts "].unique())
    print(data1["shortness of breath"].unique())
    print(data1["weight loss "].unique())
    print(data1["body feels tired"].unique())
    print(data1["lumps that appear around the armpits and neck"].unique())
    print(data1["cough and phlegm continuously for two weeks to four weeks"].unique())
    print(data1["swollen lymph nodes"].unique())
    print(data1["loss of appetite"].unique())

    def user_input():
        gender = st.sidebar.selectbox("Gender",("Female","Male"))
        fever = st.sidebar.selectbox("Fever for two weeks",(0,1))
        coughing_blood = st.sidebar.selectbox("Coughing blood",(0,1))
        sputum_mixed_with_blood = st.sidebar.selectbox("Sputum mixed with blood",(0,1))
        nightsweats = st.sidebar.selectbox("Night sweats",(0,1))
        chest_pain = st.sidebar.selectbox("Chest pain",(0,1))
        backpain_in_certain_parts = st.sidebar.selectbox("back pain in certain parts",(0,1))
        shortness_of_breath = st.sidebar.selectbox("shortness of breath",(0,1))
        weightloss = st.sidebar.selectbox("weight loss",(0,1))
        body_feels_tired = st.sidebar.selectbox("body feels tired",(0,1))
        lumps = st.sidebar.selectbox("lumps that appear around the armpits and neck",(0,1))
        cough_and_phelgm = st.sidebar.selectbox("cough and phlegm continuously for two weeks to four weeks",(0,1))
        swallen_lymph_nodes = st.sidebar.selectbox("swollen lymph nodes",(0,1))
        loss_of_appetite = st.sidebar.selectbox("loss of appetite",(0,1))
        data = {
            "Gender":gender,
            "Fever for two weeks":fever,
            "Coughing blood":coughing_blood,
            "Sputum mixed with blood":sputum_mixed_with_blood ,
            "Night sweats":nightsweats,
            "Chest pain":chest_pain,
            "back pain in certain parts":backpain_in_certain_parts,
            "shortness of breath":shortness_of_breath ,
            "weight loss":weightloss ,
            "bosy feels tired":body_feels_tired,
            "lumps that appear around the armpits and neck":lumps,
            "cough and phlegm continuously for two weeks to four weeks":cough_and_phelgm,
            "swollen lymph nodes":swallen_lymph_nodes,
            "loss of appetite":loss_of_appetite
        }
        features = pd.DataFrame(data,index=[1])
        return features
    df = user_input()
    st.subheader("User Input Parameters")
    st.write(df)


    gender_num = {"Female":0,"Male":1}
    data1["gender"] = data1["gender"].map(gender_num)

    df["Gender"] = df["Gender"].map(gender_num)

    data1.drop("no",axis=1,inplace=True)
    data1.drop("name",axis=1,inplace=True)
    data1.head()

    kmeans = KMeans(n_clusters=2,random_state=0).fit(data1)
    output = kmeans.predict(df)
    st.write
    

    def predict():
        result = "Result: "+str(output[0])
        if(result==0):
            st.success("Having Disease")
        else:
            st.success("No Disease")

    st.button("Predict",on_click=predict)
    st.write("Scroll to top of page to see the result after clicking on predict!!!")

    

