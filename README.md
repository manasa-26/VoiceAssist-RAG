 VoiceAssist-RAG
A multimodal voice-enabled assistant that combines speech recognition, retrieval-augmented generation (RAG), and text-to-speech to deliver intelligent, voice-based answers from domain-specific documents.

🚀 Features
🔍 RAG (Retrieval-Augmented Generation) pipeline to provide grounded responses using telecom_faq.txt

🎤 Whisper-based Speech-to-Text: Converts voice input (input.m4a, input.wav) into accurate transcripts

💬 Streamlit UI: Simple and interactive frontend for voice-to-answer interaction

🗣️ Text-to-Speech: Converts model-generated responses back to audio (output.mp3)

🧠 Vector-based semantic search powered by FAISS

📁 Modular architecture with a clear and maintainable structure

📁 Project Structure

call-center-rag/
├── app/
│   ├── __pycache__/           # Compiled Python files (should be gitignored)
│   ├── __init__.py            # Package initializer
│   ├── demo_runner.py         # Example pipeline runner
│   ├── embed_store.py         # Vector DB creation & loading
│   ├── rag_pipeline.py        # Main RAG orchestration logic
│   ├── text_to_speech.py      # TTS functionality
│   └── whisper_stt.py         # STT using Whisper
│
├── data/
│   └── telecom_faq.txt        # Domain knowledge source
│
├── vectorstore/
│   ├── index.faiss            # FAISS index file
│   └── index.pkl              # Metadata for vector store
│
├── input.m4a / input.wav      # Example voice input files
├── output.mp3                 # Example generated speech output
├── streamlit_app.py           # Streamlit frontend entry point
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
