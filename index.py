import streamlit as st
import time
import joblib
from pathlib import Path
import pandas as pd
import shap
from streamlit_shap import st_shap

# Define your navigation pages with an added entry for the presentation
pages = {
    "Home": [
        st.Page("about_our_project.py", title="About"),
    ],
    "Text Classification Models": [
        st.Page("relevance_detection.py", title="Relevance Model"),
        st.Page("stance_detection.py", title="Stance Model"),
        st.Page("stance_direction.py", title="Polarity Model"),
    ],
    "GoEmotions": [
        st.Page("go_emotions.py", title="GoEmotions Model"),
    ],
    "Assignment 3 Presentation": [  # New page for PDF presentation
        st.Page("presentation.py", title="Presentation"),
    ],
}

# Initialize the navigation and run the selected page
pg = st.navigation(pages)
pg.run()


                
