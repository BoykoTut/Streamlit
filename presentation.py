import streamlit as st

st.title("Assignment 3 Presentation")

# Use the raw URL for the PDF
pdf_url = "https://raw.githubusercontent.com/BoykoTut/Streamlit/5e339a92771c2c4be6bdfc29320fb9234fa92abf/Assignemnt%203%20Presentation.pdf"

st.write("## Presentation Slides")

# Embed the PDF using an iframe
st.components.v1.iframe(pdf_url, width=700, height=800)

# Optional: Download button for the PDF
st.markdown(f"[Download Presentation PDF]({pdf_url})")

