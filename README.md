# 🎙️ VoiceAssist-RAG

**VoiceAssist-RAG** is a multimodal voice-enabled assistant that combines **speech recognition**, **retrieval-augmented generation (RAG)**, and **text-to-speech** to deliver intelligent, voice-based answers from domain-specific documents.

---

## 🚀 Features

- 🔍 **RAG Pipeline**: Retrieval-Augmented Generation that provides grounded answers using `telecom_faq.txt`
- 🎤 **Speech-to-Text (STT)**: Whisper-based transcription of voice input (`input.m4a`, `input.wav`)
- 🧠 **Vector Search**: Fast and accurate semantic search using **FAISS**
- 💬 **Streamlit UI**: Clean and interactive frontend for voice-to-answer interactions
- 🗣️ **Text-to-Speech (TTS)**: Converts model-generated answers to audio output (`output.mp3`)
- 🧩 **Modular Architecture**: Easy to maintain and extend

---

## Architecture Diagram

![image](https://github.com/user-attachments/assets/dcc99358-e68d-46e1-9ff8-3d260aeefe20)


## DataFlow Diagram

![Editor _ Mermaid Chart-2025-06-22-103347](https://github.com/user-attachments/assets/e7547f38-674e-4d33-a65c-245f80145601)


## 💡 Tech Stack

- **Python**, **Streamlit**
- **OpenAI Whisper** for STT
- **FAISS** for vector-based semantic retrieval
- **LLM (OpenAI / HuggingFace)** for answer generation
- **gTTS / pyttsx3** or similar for TTS

---

## 🛠️ Installation


git clone https://github.com/yourusername/call-center-rag.git
cd call-center-rag
pip install -r requirements.txt



## 🗂️ Project Structure

![image](https://github.com/user-attachments/assets/a48aa0cd-96a4-40a1-a973-3c7590519e06)


## 📸 Screenshot

![image](https://github.com/user-attachments/assets/eb20bc54-d4c7-4219-b4f7-b7da07ade8eb)



---

## 📽️ Demo Video

https://drive.google.com/file/d/1ePg8iGRVX87NQ8dEGb70B_8Fm4PGkJf6/view?usp=sharing













