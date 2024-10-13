import streamlit as st
from transformers import pipeline

# Load the emotion classifier
emotion_classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")

# Streamlit app layout
st.title("Text Emotion Analysis")

# Create a text area for user input
input_text = st.text_area("Enter your text here:")

# Button to submit the input
if st.button("Submit"):
    if input_text:
        # Analyze the input text
        result = emotion_classifier([input_text])
        st.write("You entered:")
        st.write(input_text)
        st.write("Analysis result:")
        st.write(result)
    else:
        st.warning("Please enter some text before submitting.")


