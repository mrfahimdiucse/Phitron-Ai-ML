import streamlit as st
st.header("Audio & Video Player App")
st.divider()

audio=st.file_uploader("Upload Audio Files Here",type=['mp3','ogg'])
video=st.file_uploader("Upload Video Files Here",type=['mp4','mkv'])

play=st.button("Play Media")

if play:
    if audio or video:
        st.success("Media file loaded successfully!")
        if audio:
            st.subheader("Audio Player")
            st.audio(audio)

        if video:
            st.subheader("Video Player")
            st.video(video)

    else:
        st.error("Please upload an audio or video file first!")
        
    