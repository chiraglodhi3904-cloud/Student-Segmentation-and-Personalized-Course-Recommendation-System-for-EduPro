import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

users = pd.read_excel(
    "data/EduPro Online Platform.xlsx",
    sheet_name="Users"
)

courses = pd.read_excel(
    "data/EduPro Online Platform.xlsx",
    sheet_name="Courses"
)

transactions = pd.read_excel(
    "data/EduPro Online Platform.xlsx",
    sheet_name="Transactions"
)

learner_profile = pd.read_csv(
    "outputs/final_learner_profile.csv"
)

st.title("🏠 EduPro Dashboard")

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Users", len(users))

with col2:
    st.metric("Courses", len(courses))

with col3:
    st.metric("Transactions", len(transactions))

with col4:
    st.metric(
        "Segments",
        learner_profile["Segment"].nunique()
    )

st.markdown("---")

st.subheader("Project Overview")

st.write("""
This project demonstrates:

• Student Segmentation

• K-Means Clustering

• PCA Visualization

• Personalized Course Recommendation

• Learner Behavior Analytics
""")