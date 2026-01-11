import streamlit as st
st.header("Welocome To Login Page")
with st.form("Login"):
    n=st.text_input("Enter your user name")
    p=st.number_input("Enter your password",step=1)
    l=st.form_submit_button("Login")
if l:
    if n!="Abhishek":
        st.write("Invalid user name!!")
    elif p!=123:
        st.write("Invalid password")
    else:
        st.success("Login Successfully")
        
