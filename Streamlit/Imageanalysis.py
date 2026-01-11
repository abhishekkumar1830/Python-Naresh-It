import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
import os
import streamlit as st
from PIL import Image
load_dotenv()
genai.configure(api_key=os.getenv("newapi"))
st.title("Image Analysis...")
a = st.file_uploader("Upload your Image",type=["jpg","jpeg","png"])
if a is not None:
    #this is used because streamlit only upload file or gemini only understand image or text so it will convert the file into pil image form
    img = Image.open(a)
    #this is used to show image on streamlit app so user can see what he uploaded
    st.image(img) 
    prompt=st.text_input("Enter your prompt here")
    if prompt:
        model=genai.GenerativeModel("gemini-2.5-flash")
        response=model.generate_content([prompt,img])
        st.success("Image Analyzed Successfully")
        st.markdown(response.text)