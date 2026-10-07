import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
load_dotenv()

st.title("Gemini AI Assistant")
st.divider()

api_key=os.environ.get("GEMINI_API_KEY")

user_prompt = st.text_input("Enter your prompt:", placeholder="Ask anything...")
submit_button = st.button("Generate Response", type="primary")

client = genai.Client(api_key=api_key)

if submit_button:
    if user_prompt.strip():
        response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=user_prompt
        )    
        st.subheader("Response:")
        st.markdown(response.text)
    else:
        st.warning("Please enter a valid prompt before submitting.")