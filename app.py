import streamlit as st

# Streamlit app layout
st.title("Text Input Example")

# Create a text area for user input
input_text = st.text_area("Enter your text here:")

# Button to submit the input
if st.button("Submit"):
    if input_text:
        st.write("You entered:")
        st.write(input_text)
    else:
        st.warning("Please enter some text before submitting.")
