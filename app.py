import streamlit as st
from gtts import gTTS
from io import BytesIO

st.title("Text-to-Speech Converter")
text = st.text_area("Enter text")
tone = st.selectbox("Tone", ["neutral", "suspenseful", "inspiring"])

if st.button("Generate Speech"):
    # Generate speech directly to memory (no file save)
    audio_bytes = BytesIO()
    tts = gTTs(text, lang='en', slow=(tone == "suspenseful"))
    tts.write_to_fp(audio_bytes)  # Write to BytesIO buffer
    audio_bytes.seek(0)  # Reset pointer to start of buffer
    
    # Play and download
    st.audio(audio_bytes, format="audio/mp3")
    st.download_button(
        label="Download Audio",
        data=audio_bytes,
        file_name=f"{tone}_speech.mp3",
        mime="audio/mp3"
    )
