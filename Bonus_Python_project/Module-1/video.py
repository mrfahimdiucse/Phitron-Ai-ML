import streamlit as st

st.header("Video Gallery:")
st.divider()

videos = st.file_uploader("Enter Video File: ", type=['mp4', 'mkv'], accept_multiple_files=True)

if videos:
    cols = st.columns(len(videos))
    
    for i, video_file in enumerate(videos):
        with cols[i]:
            st.write(f"**{video_file.name}**")
            st.video(video_file)