import streamlit as st

st.title("Assignment 3 Presentation")

pdf_path = "Assignment_3_Presentation.pdf"  # Make sure this path is correct
st.write("## Presentation Slides")

# Embed the PDF with an iframe for easy viewing
st.markdown(f'<iframe src="file://{pdf_path}" width="700" height="800" style="border: none;"></iframe>', unsafe_allow_html=True)

# Optional: Download button for the PDF
with open(pdf_path, "rb") as pdf_file:
    pdf_data = pdf_file.read()
    st.download_button(label="Download Presentation PDF", data=pdf_data, file_name="Assignment_3_Presentation.pdf", mime="application/pdf")
