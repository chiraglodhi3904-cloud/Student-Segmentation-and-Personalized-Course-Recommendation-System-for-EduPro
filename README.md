#  Student Segmentation and Personalized Course Recommendation System for EduPro

An end-to-end Machine Learning project that analyzes learner behavior, segments students into meaningful groups using K-Means Clustering, and provides personalized course recommendations through an interactive Streamlit dashboard.

---

##  Project Overview

Online learning platforms serve thousands of learners with different interests, learning patterns, spending habits, and engagement levels.

This project helps EduPro:

- Identify distinct learner segments
- Understand learner behavior
- Visualize customer groups using PCA
- Recommend relevant courses based on preferences
- Enable business-driven decisions through analytics

---

##  Business Objectives

- Improve learner engagement
- Increase course enrollments
- Personalize learning experiences
- Identify high-value customers
- Support targeted marketing campaigns

---

##  Dataset Information

The project uses a synthetic EduPro dataset containing:

### Users
- UserID
- UserName
- Age
- Gender
- Email

### Courses
- CourseID
- CourseName
- CourseCategory
- CourseType
- CourseLevel
- CoursePrice
- CourseDuration
- CourseRating

### Transactions
- TransactionID
- UserID
- CourseID
- TransactionDate
- Amount
- PaymentMethod
- TeacherID

---

## Feature Engineering

The following learner-level features were created:

| Feature | Description |
|----------|-------------|
| TotalCourses | Number of courses enrolled |
| TotalSpending | Total amount spent |
| CategoryDiversity | Number of unique categories explored |
| AvgRating | Average rating of enrolled courses |
| PreferredCategory | Most enrolled category |
| PreferredLevel | Most preferred course level |

---

##  Machine Learning Pipeline

### Data Preprocessing

- Data Cleaning
- Missing Value Handling
- Feature Engineering
- Label Encoding
- Feature Scaling

### K-Means Clustering

Learners were segmented using:

- K-Means Clustering
- Elbow Method
- Silhouette Score Analysis

### Final Segments

1. Beginner Learners
2. Career Focused Learners
3. Quality Seekers
4. Inactive Learners
5. Premium Power Learners

---

##  PCA Visualization

Principal Component Analysis (PCA) was applied to reduce feature dimensions and visualize learner segments in a 2D space.

Benefits:

- Better cluster interpretation
- Easier business understanding
- Interactive visualization through Streamlit

---

##  Recommendation Engine

A personalized recommendation engine suggests courses based on:

- Course Category
- Course Level
- Course Ratings

Users can:

- Select a category
- Select a difficulty level
- View top-rated recommended courses

---

##  Streamlit Dashboard Features

###  Home Page
- Project Overview
- Business Problem
- KPI Metrics

###  Learner Segmentation
- Segment Distribution
- Segment Summary
- PCA Visualization

###  Recommendation Engine
- Category-Based Recommendations
- Level-Based Recommendations
- Top Rated Courses

###  Segment Explorer
- Explore individual learner segments
- Download segment-specific data
- Analyze learner characteristics

---

##  Project Structure

```text
EDUPRO PROJECT1
│
├── app/
│   ├── pages/
│   │   ├── 1_Home.py
│   │   ├── 2_Learner_Segmentation.py
│   │   ├── 3_Recommendation_Engine.py
│   │   └── 4_Segment_Explorer.py
│   │
│   └── streamlit_app.py
│
├── data/
│   └── EduPro Online Platform.xlsx
│
├── notebooks/
│   ├── 01_data_loading.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_clustering.ipynb
│   └── 04_recommendation_system.ipynb
│
├── outputs/
│   ├── learner_profile.csv
│   ├── final_learner_profile.csv
│   └── pca_visualization.csv
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

##  Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Streamlit
- Jupyter Notebook
- Git
- GitHub

---

##  Installation

Clone the repository:

```bash
git clone https://github.com/chiraglodhi3904-cloud/Student-Segmentation-and-Personalized-Course-Recommendation-System-for-EduPro.git
```

Move into the project directory:

```bash
cd Student-Segmentation-and-Personalized-Course-Recommendation-System-for-EduPro
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the dashboard:

```bash
streamlit run app/streamlit_app.py
```

---

##  Key Learnings

- Customer Segmentation using K-Means
- Feature Engineering
- Cluster Evaluation
- PCA Visualization
- Recommendation Systems
- Streamlit Dashboard Development
- Git & GitHub Workflow

---

##  Future Improvements

- Collaborative Filtering
- Hybrid Recommendation System
- User Login System
- Real-Time Analytics
- Deployment on Streamlit Cloud
- Advanced Business Intelligence Dashboard

---

##  Author

**Chirag Verma**

Electronics & Communication Engineering  
IIIT Manipur

Passionate about:
- Machine Learning
- Data Analytics
- Recommendation Systems
- AI Applications

---

⭐ If you found this project useful, consider giving it a star.
