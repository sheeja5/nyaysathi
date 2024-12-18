import streamlit as st
import google.generativeai as genai

question = st.text_input()
prompt = f"{question} you are an expert in legal assitance of India you are being creted to help people get justice for free hereby you are called Nyaysathi"
genai.configure(api_key="AIzaSyD_1JOiWc67HjO6G34ZHVXhULbcoS19ji8")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(prompt)
print(response.text) 
