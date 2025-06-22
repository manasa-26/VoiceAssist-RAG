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

## 🗂️ Project Structure

call-center-rag/
├── app/
│ ├── pycache/ # Compiled Python cache (gitignored)
│ ├── init.py # Package initializer
│ ├── demo_runner.py # End-to-end RAG pipeline runner
│ ├── embed_store.py # Vector DB creation & loading logic
│ ├── rag_pipeline.py # RAG orchestration (retrieval + generation)
│ ├── text_to_speech.py # TTS module (text to audio)
│ └── whisper_stt.py # STT module using OpenAI Whisper
│
├── data/
│ └── telecom_faq.txt # Domain-specific knowledge base
│
├── vectorstore/
│ ├── index.faiss # FAISS vector index
│ └── index.pkl # Metadata for vector search
│
├── input.m4a / input.wav # Example voice input files
├── output.mp3 # Example generated audio response
├── streamlit_app.py # Streamlit UI frontend
├── requirements.txt # Required Python packages
└── README.md # Project documentation



