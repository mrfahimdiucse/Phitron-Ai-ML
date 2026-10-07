import streamlit as st
st.header("Images Gallary:")
st.divider()
images=st.file_uploader("Enter You Image File: ",type=['jpg','jpeg','png','mkv'],accept_multiple_files=True)
if images:
    col=st.columns(len(images))
    for i,image in enumerate(images):
        with col[i]:
            st.image(image)