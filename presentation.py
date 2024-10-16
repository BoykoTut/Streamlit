import streamlit as st
from pdf2image import convert_from_path

# Set the title of the Streamlit app
st.title("Assignment 3 Presentation")

# Path to the PDF file (you can also use the GitHub raw link)
pdf_path = "Assignemnt_3_Presentation.pdf"  # Make sure this is the correct path

# Convert PDF to images
images = convert_from_path(pdf_path)

# Display the images in the Streamlit app
st.write("## Presentation Slides")
for i, image in enumerate(images):
    st.image(image, caption=f'Slide {i + 1}', use_column_width=True)

