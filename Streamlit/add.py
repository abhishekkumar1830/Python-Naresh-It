import streamlit as st
n1=st.number_input("Enter the First number")
n2=st.number_input("Enter the Second number")
with st.form("Addition"):
    add=n1+n2
    addittion=st.form_submit_button("add")
if addittion:
    st.success("Enterd successfully")
    st.write("### Your result")
    st.write(int(add))