import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
load_dotenv()

st.title("Professional Sentence Enhancer")
st.divider()
user_sentence = st.text_input(
    "Enter a sentence:", 
    placeholder="e.g., i want job"
)
enhance_button = st.button("Improve Sentence", type="primary")
client = genai.Client()

if enhance_button:
    if user_sentence.strip():
        prompt = f"Improve this sentence professionally: '{user_sentence}'" 
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt
        )
        st.subheader("Improved Version:")
        st.write(response.text)
    else:
        st.warning("Please enter a sentence to improve.")