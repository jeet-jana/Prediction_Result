import streamlit as st

st.title("Student Pass Prediction System")

st.write("This application uses a Machine Learning model trained on student academic and behavioral data to predict whether a student is likely to pass or fail. Enter details such as study hours, attendance, previous performance, and other factors to receive a prediction along with the model's confidence score.")

st.subheader("Enter you UID:")
Student_id = st.text_input("")


st.subheader("Enter Your Gender")
Gender = st.selectbox("__________________",["Male","Female"])


st.write("_________________")


st.subheader("Select your age")
Student_age = st.slider("___________",0,100,18)


st.write("_________________")

st.subheader("Enter The Study Hour Per Week")
Study_hour = st.number_input("Give Me in Hour",max_value=168)

st.write("_________________")

st.subheader("Attendance_rate")
attendance = st.number_input("",max_value=100)


st.write("_________________")
st.subheader("Enter Your Parent_Education")
Education = st.selectbox("__________________",["Bachelor","High School"])

st.write("_________________")
st.subheader("Can You Have Internet")
Access = st.radio("",["Yes","No"],key = "Access")


st.write("_________________")
st.subheader("Can You Join Extracurricular")
Curricular = st.radio("",["Yes","No"],key = "Curricular")

st.write("_________________")

st.subheader("Previous Year Score")
Previou_result = st.slider("___________",0,100,60)



# -------------Convertion-----------

Gender = [1 if Gender == "Male" else 0]
# Student_age
# Study_hour
# attendance
Education = [1 if Education == "Bachelor" else 0]
Access = [1 if Access == "Yes" else 0]
Curricular = [1 if Curricular == "Yes" else 0]
# Previou_result


# ------------Normal-standard-deviation data---

list=[[Gender[0],Student_age,Study_hour,attendance,Education[0],Access[0],Curricular[0],Previou_result]]
st.write("",list)

# ---------------
import joblib
import time

audio_file = open("Sound1.m4a","rb")
audio_bytes = audio_file.read()

if st.button("Submit"):

    st.audio(audio_bytes, format="audio/m4a", autoplay=True)

    st.subheader(f"Prediction Start under 5 second")


    

    # for i in range(5,0,-1):
    #     st.write(i)
    #     time.sleep(0.5)
    with st.spinner("Processing"):
        time.sleep(6)
        model = joblib.load("Pass_model.pkl")
        stand = joblib.load("Standard__Normal_data.pkl")


        list1 = stand.transform(list)


        Data =  model.predict(list1)
        Data1 = model.predict_proba(list1)
        time.sleep(3)

    st.success("Prediction Start")
    time.sleep(1)

    if Data[0] == 1:
        st.success("You May Pass In The Exam")
        st.balloons()
    else:
        st.error("Better Luck Next Time🤣🤣🤣")


    st.subheader(f"UID = :{Student_id}")
    st.success(f"Pass probabilty ={Data1[0][1]*100:.2f}% ")
    st.error(f"Fail Probability={Data1[0][0]*100:.2f}%")