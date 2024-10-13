import streamlit as st
from transformers import pipeline

# Load the emotion classifier
emotion_classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")

# Streamlit app layout
st.title("Emotion Analysis App")

# Create a text area for user input
input_text = st.text_area("Enter your text here:")

# Button to submit the input
if st.button("Submit"):
    if input_text:
        # Classify the input text
        result = emotion_classifier([input_text])
        # Display the results
        st.write("Analysis Result:")
        st.write(result)
    else:
        st.warning("Please enter some text before submitting.")

