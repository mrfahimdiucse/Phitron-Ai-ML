import streamlit as st
st.header("Input Element of Streamlit:",anchor=False)
st.divider()
name=st.text_input("Enter Your Name: ",placeholder="Sadik Hasan")
age=st.number_input("Enter Your Age :",placeholder="21",value=None)
button=st.button(":red[Confirm]")
if button:
    st.write(f"Name is : {name}")
    st.write(f"Age is : {age}")
