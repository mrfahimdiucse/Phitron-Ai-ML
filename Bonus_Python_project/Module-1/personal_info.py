import streamlit as st
st.header("Personal Info Card App: ")
st.divider()
name = st.text_input("Enter Your Name: ", placeholder="type your full name")
age = st.number_input("Enter Your Age: ", value=None, placeholder="type your age here")
profession = st.selectbox("Choose Your Profession: ", ['Student', 'Employee', 'Businessman', 'Freelancer'], index=None)

button = st.button(":red-background[Submit]",type="primary")

if button:
    if name and age and profession:
        st.success("Successfully Input Done")
        st.write(f"**Name :** {name}")
        st.write(f"**Age :** {int(age)}")
        st.write(f"**Profession :** {profession}")
    else:
        st.warning("Please Fill Up the Form")