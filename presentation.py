import streamlit as st

# Set the title of the Streamlit app
st.title("Presentation Slides")

# Use the raw URL for the PDF
pdf_url = "https://raw.githubusercontent.com/BoykoTut/Streamlit/5e339a92771c2c4be6bdfc29320fb9234fa92abf/Assignemnt%203%20Presentation.pdf"


# HTML code to embed the PDF
pdf_embed_code = f"""
<iframe src="{pdf_url}" width="700" height="800" style="border:none;"></iframe>
"""

# Use st.components.v1.html to render the HTML code
st.components.v1.html(pdf_embed_code, height=800)

