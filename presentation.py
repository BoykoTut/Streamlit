import streamlit as st

# Display the PDF presentation using an iframe
st.title("Assignment 3 Presentation")

pdf_path = "Assignment_3_Presentation.pdf"  # Ensure this is the correct file path
st.write("## Presentation Slides")

# Embed the PDF with an iframe for easy viewing
st.components.v1.iframe(f"file://{pdf_path}", width=700, height=800)

# Optional: Download button for the PDF
with open(pdf_path, "rb") as pdf_file:
    pdf_data = pdf_file.read()
    st.download_button(label="Download Presentation PDF", data=pdf_data, file_name="Assignment_3_Presentation.pdf", mime="application/pdf")
