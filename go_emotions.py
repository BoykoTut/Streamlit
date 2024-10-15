import streamlit as st
import joblib
from pathlib import Path
import pandas as pd
import shap
from streamlit_shap import st_shap
from transformers import pipeline  # Make sure to install the transformers library

# Load the emotion classifier
emotion_classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")

sample_dict = {"Many researchers believe that PTLDS symptoms actually have nothing to do...":"Many researchers believe that PTLDS symptoms actually have nothing to do with Lyme disease, attributing these symptoms instead to other underlying conditions such as chronic fatigue syndrome, fibromyalgia, or autoimmune disorders.",
               "PLTDS is caused by clusters of Lyme bacteria that resist traditional methods of...":"PTLDS is caused by clusters of Lyme bacteria that resist traditional methods of antibiotic treatment, leading to persistent symptoms due to ongoing infection and inflammation.",
               "The hypothesis of PTLDS has been thouroughly refuted, with evidence...":"The hypothesis of PTLDS has been thoroughly refuted, with evidence suggesting that the symptoms often attributed to this condition are more likely caused by alternative diagnoses such as immune dysfunction, chronic fatigue syndrome, or psychological factors."}

# GoEmotions page content
def go_emotions_page():
    st.title("Text Emotion Analysis")

    # Allow the user to select one of the sample abstracts
    selected_abstract = st.radio("Choose an abstract to analyze:", list(sample_dict.keys()))

    # Display the selected abstract
    st.write("**Selected Abstract:**")
    st.write(sample_dict[selected_abstract])

    # Analyze the selected abstract using the emotion classifier
    if st.button("Analyze"):
        # Use the selected abstract for emotion analysis
        result = emotion_classifier([sample_dict[selected_abstract]])

        # Extract label and score
        label = result[0]['label']
        score = result[0]['score']

        # Display results in a user-friendly format
        st.subheader("Analysis Result:")
        st.write(f"**Emotion Detected:** {label}")
        st.write(f"**Confidence Score:** {score:.2f}")  # Format score to 2 decimal places

# Ensure the GoEmotions page displays its content
if st.session_state.get("current_page") == "GoEmotions Model":
    go_emotions_page()