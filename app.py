import streamlit as st
from transformers import pipeline


# Load the emotion classifier
emotion_classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")


# Streamlit app layout
st.title("Text Input Example")

# Create a text area for user input
input_text = st.text_area("Enter your text here:")

# Button to submit the input
if st.button("Analyze Emotion"):
    if input_text:
        # Classify the emotion
        result = emotion_classifier([input_text])
        
        # Display the results
        st.write("You entered:")
        st.write(input_text)
        
        # Display the emotion classification results
        st.write("Emotion Classification Result:")
        st.json(result)  # Displaying the result in a more readable format
    else:
        st.warning("Please enter some text before submitting.")
