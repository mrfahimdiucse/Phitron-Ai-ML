import streamlit as st
st.header("Selection Profile:")
st.divider()
select1=st.selectbox("Enter Your Gender: ",("Male","Female","Trans-Gender"),index=None)
select2=st.selectbox("Enter Your Profession: ",("Student","Teacher","Banker"),index=None)
select3=st.selectbox("Enter Your Relegion: ",("Muslim","Hindu"),index=None)

if select1 and select2 and select3:
    st.markdown(f"**Gender**: {select1}")
    st.markdown(f"**Profession**: {select2}")
    st.markdown(f"**Relegion**: {select3}")
