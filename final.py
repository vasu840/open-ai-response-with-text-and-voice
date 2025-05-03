import google.generativeai as genai
import pyttsx3

# Replace with your real Gemini API key from https://makersuite.google.com/app/apikey
genai.configure(api_key="AIzaSyBoIGkBKJax6Zhs8-6pcgfxgLyqEqdqt1E")

# Initialize Gemini model (use correct model ID)
model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

# Initialize text-to-speech
engine = pyttsx3.init()

def speak(text):
    print("🤖 Gemini:", text)
    engine.say(text)
    engine.runAndWait()

def ask_gemini(prompt):
    try:
        chat = model.start_chat(history=[])
        response = chat.send_message(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"

# Start interaction
speak("Hello! I'm your AI assistant. Ask me anything.")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in ["exit", "quit", "bye"]:
        speak("Goodbye!")
        break
    reply = ask_gemini(user_input)
    speak(reply)
