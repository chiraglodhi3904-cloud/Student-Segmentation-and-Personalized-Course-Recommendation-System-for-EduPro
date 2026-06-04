import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

learner_profile = pd.read_csv(
    "outputs/final_learner_profile.csv"
)

st.title("🔍 Segment Explorer")

st.markdown("---")

selected_segment = st.selectbox(
    "Select Learner Segment",
    sorted(
        learner_profile["Segment"].unique()
    )
)

filtered_users = learner_profile[
    learner_profile["Segment"]
    == selected_segment
]

st.success(
    f"Total Learners: {len(filtered_users)}"
)

# Metrics

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Average Courses",
        round(
            filtered_users["TotalCourses"]
            .mean(),
            2
        )
    )

with col2:
    st.metric(
        "Average Spending",
        round(
            filtered_users["TotalSpending"]
            .mean(),
            2
        )
    )

with col3:
    st.metric(
        "Average Rating",
        round(
            filtered_users["AvgRating"]
            .mean(),
            2
        )
    )

st.markdown("---")

st.subheader("Learners")

st.dataframe(
    filtered_users.head(50),
    use_container_width=True
)

st.info(
    f"Showing first 50 of {len(filtered_users)} learners"
)

# Download Button

csv = filtered_users.to_csv(
    index=False
)

st.download_button(
    label="📥 Download Segment Data",
    data=csv,
    file_name="segment_data.csv",
    mime="text/csv"
)

st.subheader("📈 Segment Statistics")

stats = filtered_users[
    [
        "TotalCourses",
        "TotalSpending",
        "AvgRating"
    ]
].describe()

st.dataframe(
    stats,
    use_container_width=True
)