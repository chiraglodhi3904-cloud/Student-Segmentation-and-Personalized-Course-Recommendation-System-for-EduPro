import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

learner_profile = pd.read_csv(
    "outputs/final_learner_profile.csv"
)

pca_df = pd.read_csv(
    "outputs/pca_visualization.csv"
)

st.title("👥 Learner Segmentation")

st.markdown("---")

# Segment Distribution

st.subheader("Learner Segment Distribution")

segment_counts = (
    learner_profile["Segment"]
    .value_counts()
)

fig, ax = plt.subplots(figsize=(10,5))

segment_counts.plot(
    kind="bar",
    ax=ax
)

ax.set_xlabel("Segments")
ax.set_ylabel("Number of Learners")
ax.set_title("Learner Segment Distribution")

plt.xticks(rotation=25)

st.pyplot(fig)

# Segment Summary

st.markdown("---")

st.subheader("Segment Summary")

segment_summary = (
    learner_profile.groupby("Segment")
    .agg({
        "TotalCourses":"mean",
        "TotalSpending":"mean",
        "CategoryDiversity":"mean",
        "AvgRating":"mean"
    })
    .round(2)
)

segment_summary.columns = [
    "Avg Courses",
    "Avg Spending",
    "Category Diversity",
    "Avg Rating"
]

st.dataframe(
    segment_summary,
    use_container_width=True
)

# PCA Visualization

st.markdown("---")

st.subheader("PCA Cluster Visualization")

fig, ax = plt.subplots(figsize=(10,6))

segments = pca_df["Segment"].unique()

for segment in segments:

    temp = pca_df[
        pca_df["Segment"] == segment
    ]

    ax.scatter(
        temp["PCA1"],
        temp["PCA2"],
        label=segment,
        alpha=0.6
    )

ax.set_xlabel("PCA 1")
ax.set_ylabel("PCA 2")

ax.set_title(
    "Learner Segments Visualization"
)

ax.legend()

st.pyplot(fig)

st.markdown("---")

st.subheader(" Business Insights")

st.info("""
 Premium Power Learners:
Highest spending and most engaged learners.

 Career Focused Learners:
Goal-oriented learners with focused course selection.

 Beginner Learners:
New users exploring the platform.

 Quality Seekers:
Learners preferring highly-rated content.

 Inactive Learners:
Low engagement and low spending users.
""")