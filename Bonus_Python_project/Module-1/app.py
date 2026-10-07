import os
from dotenv import load_dotenv
import streamlit as st
from google import genai

load_dotenv()

client = genai.Client()

response = client.models.generate_content(
model="gemini-3.8-flash", 
contents="Write something about gemini in 100 words")
    
st.markdown(response.text)