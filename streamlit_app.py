import streamlit as st
import os
from app.whisper_stt import transcribe
from app.rag_pipeline import generate_response
from app.text_to_speech import speak

st.set_page_config(page_title="Call Center RAG", layout="centered")

st.title("📞 Call Center AI Assistant")
st.markdown("Speak or upload an audio file to get help like a real call center agent.")

uploaded_file = st.file_uploader("Upload an audio file (WAV only)", type=["wav"])

if uploaded_file:
    # Save uploaded file
    input_audio_path = "input.wav"
    with open(input_audio_path, "wb") as f:
        f.write(uploaded_file.read())

    st.audio(input_audio_path, format="audio/wav")
    st.success("Audio uploaded!")

    # Transcribe
    with st.spinner("Transcribing..."):
        user_query = transcribe(input_audio_path)
        st.write("**You said:**", user_query)

    # RAG response
    with st.spinner("Generating response..."):
        bot_response = generate_response(user_query)
        st.write("**Bot says:**", bot_response)

    # Text to speech (optional)
    if st.button("🔊 Hear the response"):
        speak(bot_response)
        st.audio("output.mp3", format="audio/mp3")
