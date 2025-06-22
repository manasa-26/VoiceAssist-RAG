from gtts import gTTS

def speak(text, filename="output.mp3"):
    tts = gTTS(text)
    tts.save(filename)
    print(f"[INFO] Audio saved to {filename}")
