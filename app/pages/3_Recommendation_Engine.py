import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

courses = pd.read_excel(
    "data/EduPro Online Platform.xlsx",
    sheet_name="Courses"
)

st.title("🎯 Personalized Course Recommendation")

st.markdown("---")

st.info(
    """
    Select a course category and level.
    The system will recommend the highest-rated courses.
    """
)

# Category Selection

selected_category = st.selectbox(
    "Select Course Category",
    sorted(
        courses["CourseCategory"].unique()
    )
)

# Level Selection

selected_level = st.selectbox(
    "Select Course Level",
    sorted(
        courses["CourseLevel"].unique()
    )
)

# Recommendation Logic

recommended_courses = courses[
    (
        courses["CourseCategory"]
        == selected_category
    )
    &
    (
        courses["CourseLevel"]
        == selected_level
    )
]

recommended_courses = recommended_courses.sort_values(
    by="CourseRating",
    ascending=False
)

st.markdown("---")

st.subheader("Recommended Courses")

if len(recommended_courses) > 0:

    st.success(
        f"{len(recommended_courses)} courses found"
    )

    st.dataframe(
        recommended_courses[
            [
                "CourseName",
                "CourseCategory",
                "CourseLevel",
                "CourseRating",
                "CoursePrice",
                "CourseDuration"
            ]
        ].head(10),
        use_container_width=True
    )

else:

    st.warning(
        "No courses available for selected category and level."
    )