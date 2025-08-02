import streamlit as st
import pickle as p
import zipfile
import pickle

with zipfile.ZipFile("regressor.zip", "r") as zipf:
    with zipf.open("regressor.pkl") as f:
        model = pickle.load(f)


with open("data.pkl","rb") as f:
    data=p.load(f)
with open("label_encode.pkl","rb") as f:
    le=p.load(f)
# with open("regressor.pkl","rb") as f:
#     reg=p.load(f)
with open("standard_scaler.pkl","rb") as f:
    ss=p.load(f)

from sklearn.preprocessing import LabelEncoder,StandardScaler
# ss.fit(data["age"])
# ss.fit(data["working_hours"])
st.title("Predict Your Salary")
education=st.selectbox("EDUCATON",list(data["education_level"]))
le.fit(data["education_level"])
education=le.transform([education])[0]
le.fit(data["industry"])
industry=st.selectbox("Industry",list(data["industry"]))
industry=le.transform([industry])[0]
le.fit(data["job_title"])
job_title=st.selectbox("job_title",list(data["job_title"]))
job_title=le.transform([job_title])[0]
le.fit(data["location"])
location=st.selectbox("location",list(data["location"]))
location=le.transform([location])[0]
le.fit(data["company_size"])
company_size=st.selectbox("company_size",list(data["company_size"]))
company_size=le.transform([company_size])[0]
certifications=st.selectbox("certifications",list(data["certifications"]))
years_experience=st.selectbox("years_experience",list(data["years_experience"]))
selected_hours = st.selectbox("Working Hours", sorted(set(data["working_hours"])))
working_hours_scaled = ss.transform([[selected_hours]])[0][0]
age = st.selectbox("Age", sorted(set(data["age"])))  # <- Use Series, not DataFrame
age_scaled = ss.transform([[age]])[0][0]
# education_level,years_experience,job_title,industry,location,company_size,certifications,age,working_hours
if st.button("predict my salary"):
    input_data = [[
        education,
        years_experience,
        job_title,
        industry,
        location,
        company_size,
        certifications,
        age_scaled,
        working_hours_scaled
    ]]
    salary = model.predict(input_data)[0]
    st.success(f"Predicted Salary: ₹{salary:,.2f}")



# years_experience,,,,age,working_hours,