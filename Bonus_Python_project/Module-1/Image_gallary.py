import streamlit as st
st.header("Image Gallary App")
st.divider()
images=st.file_uploader("Upload Your Images",type=['jpg','jpeg','png'],accept_multiple_files=True)

if images:
    if len(images)==3:
        col=st.columns(len(images))
        st.success("Succefully Added 3 Pictures")
        for i,image in enumerate(images):
            with col[i]:
                st.image(image)
    elif len(images)<3:
        st.warning(f"Please upload 3 images. You uploaded only {len(images)}.")
    else:
        st.error("You can not Upload more then 3 images!")


