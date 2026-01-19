import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import random

# 🔹 Voice Engine Setup
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Male voice (0) / Female voice (1)

# 🔹 Speak Function
def speak(text):
    print("AI: " + text)
    engine.say(text)
    engine.runAndWait()

# 🔹 Listen Function
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am Listening sir...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language="english")
        print("Tumne kaha: " + command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Maaf kijiye, main sun nahi paya. Kripya dobara bolein.")
        return None
    except sr.RequestError:
        speak("Speech service are down please internet check karein.")
        return None
op_any = random.choice

# 🔹 Open Apps or Websites
def perform_action(command):
    if "notepad" in command:
        speak("Notepad khol raha hoon...")
        os.system("notepad")

    elif "chrome" in command:
        speak("Chrome khol raha hoon...")
        os.system("start chrome")

    elif "youtube" in command:
        speak("YouTube khol raha hoon...")
        webbrowser.open("https://www.youtube.com")

    elif "google" in command:
        speak("Google khol raha hoon...")
        webbrowser.open("https://www.google.com")


    elif "open" in command:
        speak("Google khol raha hoon...")
        webbrowser.open(op_any)


    elif "bye" in command or "band karo" in command:
        speak("Achha, main ja raha hoon! Phir milte hain!")
        exit()

    else:
        speak("Maaf kijiye, yeh command samajh nahi aaya.")

# 🔹 Main Loop
speak("hii! I'am your  AI assistant hoon. you can tell me any command.")
while True:
    user_command = listen()
    if user_command:
        perform_action(user_command)
