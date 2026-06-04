import streamlit as st

st.set_page_config(
    page_title="EduPro Dashboard",
    page_icon="🎓",
    layout="wide"
)

# Header

st.title("🎓 EduPro ML Dashboard")

st.markdown("""
### Student Segmentation & Personalized Course Recommendation System

An end-to-end Machine Learning project that analyzes learner behavior,
segments students using K-Means Clustering, and recommends relevant courses
based on learner preferences.
""")

st.markdown("---")

# Highlights

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
    ### 👥 Learner Segmentation

    Cluster students into meaningful learner groups using K-Means Clustering.
    """)

with col2:
    st.success("""
    ### 🎯 Smart Recommendations

    Recommend the highest-rated courses based on category and level.
    """)

with col3:
    st.warning("""
    ### 📊 Analytics Dashboard

    Visualize learner behavior through PCA and interactive dashboards.
    """)

st.markdown("---")

# Tech Stack

st.subheader("⚙️ Technology Stack")

tech1, tech2, tech3, tech4 = st.columns(4)

with tech1:
    st.metric("Python", "3.14.5")

with tech2:
    st.metric("Pandas", "Data Analysis")

with tech3:
    st.metric("Scikit-Learn", "ML Engine")

with tech4:
    st.metric("Streamlit", "Dashboard")

st.markdown("---")

# Workflow

st.subheader(" Project Workflow")

st.markdown("""
1.  Data Collection

2.  Data Cleaning & Preprocessing

3.  Feature Engineering

4.  K-Means Clustering

5.  PCA Visualization

6.  Course Recommendation

7.  Interactive Dashboard
""")

st.markdown("---")

# Sidebar Guide

st.subheader(" Navigation Guide")

st.markdown("""
Use the sidebar to explore the project:

-  **Home** → Project Overview
-  **Learner Segmentation** → Clustering Analysis
-  **Recommendation Engine** → Course Recommendations
-  **Segment Explorer** → Explore Learner Groups
""")

st.success("Project Successfully Built Using Machine Learning + Streamlit")