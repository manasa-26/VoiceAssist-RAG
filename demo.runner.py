from whisper_stt import transcribe
from embed_store import build_vectorstore
from rag_pipeline import query_with_context
from text_to_speech import speak
import os

def run_demo():
    print("[INFO] Building vectorstore...")
    build_vectorstore()

    print("[INFO] Transcribing audio...")
    user_query = transcribe("input.wav")
    print(f"[USER]: {user_query}")

    print("[INFO] Generating response via RAG...")
    answer = query_with_context(user_query)
    print(f"[BOT]: {answer}")

    print("[INFO] Speaking response...")
    speak(answer)

if __name__ == "__main__":
    run_demo()
