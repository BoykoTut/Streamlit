import streamlit as st
from transformers import pipeline
import nltk
from nltk.tokenize import word_tokenize

# Download NLTK data files (only needs to be run once)
nltk.download('punkt')

# Load the emotion classifier
emotion_classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")

# List of keywords associated with 'fear'
fear_keywords = ['fear', 'scared', 'afraid', 'terrified', 'anxious', 'panic']

# Streamlit app layout
st.title("Text Emotion Analysis")

# Create a text area for user input
input_text = st.text_area("Enter your text here:")

# Button to submit the input
if st.button("Submit"):
    if input_text:
        # Analyze the input text
        result = emotion_classifier([input_text])
        
        # Extract label and score
        label = result[0]['label']
        score = result[0]['score']

        # Display results in a user-friendly format
        st.subheader("Analysis Result:")
        st.write(f"**Emotion Detected:** {label}")
        st.write(f"**Confidence Score:** {score:.2f}")  # Format score to 2 decimal places

        # If the detected emotion is 'fear', find related words
        if label.lower() == 'fear':
            words = word_tokenize(input_text.lower())
            related_words = [word for word in words if word in fear_keywords]
            if related_words:
                st.write("**Words related to 'fear':**")
                st.write(", ".join(related_words))
            else:
                st.write("No specific words related to 'fear' were found.")
    else:
        st.warning("Please enter some text before submitting.")

