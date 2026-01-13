import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()
genai.configure(api_key=os.getenv("GEMNI_API_KEY"))
st.title("Gemni Text Generator")
prompt=st.text_input("Ask Your Question")
if prompt:
    model=genai.GenerativeModel("gemini-2.5-flash")
    response=model.generate_content(prompt)
    st.markdown(response.text)