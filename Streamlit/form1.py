import streamlit as st

# TITLE 
st.title("Student Registration Form")
st.write("🎉 Happy New Year 🎉")

# HEADER 
st.header("Fill Your Form Details Carefully")
st.text("Enter your details below")

#FORM START 
#with st.form controls the output if we not write this then every time if we enter some input page will refresh without clicking submit button
with st.form("user_form"):

    # TEXT INPUT
    name = st.text_input("Enter Your Name")

    # NUMBER INPUT
    age = st.number_input("Enter Your Age", min_value=1, max_value=100)

    # SELECT BOX
    city = st.selectbox(
        "Choose Your City",
        ["Bihar", "Hyderabad", "Dehradun", "Bangalore"]
    )

    # RADIO BUTTON- can  choose only one option
    gender = st.radio(
        "Choose Your Gender",
        ["Male", "Female", "Others"]
    )

    # CHECKBOXES-can choose multiple option
    st.text("Choose Your Subjects")
    maths = st.checkbox("Maths")
    physics = st.checkbox("Physics")
    chemistry = st.checkbox("Chemistry")
    biology = st.checkbox("Biology")

    # SUBMIT BUTTON-this is connecting the form with button if click returns true and give output
    submit = st.form_submit_button("Submit")

#AFTER SUBMIT 
if submit:
    st.success("Details submitted successfully ✅")

    st.write("### Your Details")
    st.write("Name:", name)
    st.write("Age:", age)
    st.write("City:", city)
    st.write("Gender:", gender)

    subjects = []
    if maths:
        subjects.append("Maths")
    if physics:
        subjects.append("Physics")
    if chemistry:
        subjects.append("Chemistry")
    if biology:
        subjects.append("Biology")

    st.write("Subjects:", subjects)
