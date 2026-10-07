import streamlit as st
st.header("Audio Gallery:")
st.divider()
audios = st.file_uploader("Enter Audio File: ", type=['mp3', 'wav', 'ogg'], accept_multiple_files=True)

if audios:
    cols = st.columns(len(audios))
    
    for i, audio_file in enumerate(audios):
        with cols[i]:
            st.write(f"**{audio_file.name}**")
            st.audio(audio_file)