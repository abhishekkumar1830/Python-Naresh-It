import streamlit as st
import random
st.header("Find Average Below")
with st.form("Average"):
    n1=st.number_input("Enter the first number",step=1)
    n2=st.number_input("Enter the second number",step=1)
    n3=st.number_input("Enter the third number",step=1)
    avg=(n1+n2+n3)/3
    avrg=st.form_submit_button("Find Average")
if avrg:
    st.success("Enterd the value successfully..")
    st.write("### Your average result")
    st.write(int(avg))

st.header("Find Area Of Triangle Below")
with st.form("Area of triangle"):
    pi=st.number_input("Enter the pi value")
    r=st.number_input("Enter the radius")
    area=pi*r*r
    Area=st.form_submit_button("Find Area Of Triang")
if Area:
    st.success("You Entered successfully")
    st.write("### Your area of triangle result")
    st.write(area)

st.header("Calculate Total Bill Below")
with st.form("totalbill"):
    bill=st.number_input("Enter the total bill",step=1)
    tip=st.number_input("Enter the tip you gave",step=1)
    total=bill+tip
    Total=st.form_submit_button("Add Total Bill")
if Total:
    st.success("Amounts Entered Successfully")
    st.write("### Your total bill")
    st.write(total)

st.header("Calculate Tax Amount Below")
with st.form("tax"):
    sal=st.number_input("Enter your salary",step=1)
    tax=st.number_input("Enter your tax percentage",step=1)
    tax_amo=sal*tax/100
    cal=st.form_submit_button("Calulate Tax Amount")
if cal:
    st.success("Entered values successfully..")
    st.write("### Your Total Tax Amount")
    st.write(tax_amo)

st.header("Calculate Even or Odd Below")
with st.form("Even"):
    n1=st.number_input("Enter the Number",step=1)
    if n1%2==0:
        print("Even num")
    else:
        print("Odd num")
    Che=st.form_submit_button("Check")
if Che:
    st.success("Values Entered Successfully")
    st.write("### Your result")
    if n1%2==0:
        st.write("Even number")
    else:
        st.write("Odd number")

st.header ("Play Win or Loss Game")
with st.form("game"):
    n=st.number_input("Enter the number",step=1)
    n2=random.randint(1,10)
    p=st.form_submit_button("Play")
if p:
    st.success("You Entered Number Successfully...")
    st.write("### Your Result")
    if n==n2:
        st.write("You Won")
    else:
        st.write("You Loss")