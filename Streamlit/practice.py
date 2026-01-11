import google.generativeai as genai
from dotenv import load_dotenv
import os
import streamlit as st
from PIL import Image
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API"))
st.title("Image Analysis")
a=st.file_uploader("upload image",type="jpg")
if a is not None:
    img=Image.open(a)
    st.image(img)
    prompt=st.text_input("Enter the Prompt")
    if prompt:
        model=genai.GenerativeModel("gemini-2.5-flash")
        response=model.generate_content([prompt,img])
        st.success("Image Analyzed Successfully..")
        st.markdown(response.text)
