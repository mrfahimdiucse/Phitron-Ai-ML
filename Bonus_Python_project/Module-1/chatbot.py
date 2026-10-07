import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

st.header("Welcome To Gemini Chatbot App")
st.divider()

query = st.text_input("Enter Your Query Here:", placeholder="Ask anything...")
button = st.button("Search", type="primary")

client = genai.Client()

if button:
    if query.strip():
        response = client.models.generate_content(
            model="gemini-3.8-flash", 
            contents=query
        )
        st.markdown(response.text)
    else:
        st.warning("Please enter a query first.")