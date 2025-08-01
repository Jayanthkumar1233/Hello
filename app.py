import streamlit as st
from gtts import gTTS
from io import BytesIO

st.title("Text-to-Speech Converter")
text = st.text_area("Enter text")
tone = st.selectbox("Tone", ["neutral", "suspenseful", "inspiring"])

if st.button("Generate Speech"):
    tts = gTTS(text, lang='en', slow=(tone == "suspenseful"))
    audio_bytes = BytesIO()
    tts.write_to_fp(audio_bytes)
    st.audio(audio_bytes, format="audio/mp3")
    st.download_button("Download", audio_bytes, file_name=f"{tone}_speech.mp3")
