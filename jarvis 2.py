import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import time
import pyautogui

# Initialize the speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)  # Adjust voice speed
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Set voice

def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio, language='hi-IN')
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("मुझे समझ नहीं आया, कृपया फिर से कहें।")
            return None
        except sr.RequestError:
            speak("सर्वर से जुड़ने में समस्या हो रही है।")
            return None

def open_application(app_name):
    if "notepad" in app_name:
        os.system("notepad")
        speak("नोटपैड खोल रहा हूँ।")
    elif "chrome" in app_name:
        os.system("start chrome")
        speak("क्रोम ब्राउज़र खोल रहा हूँ।")
    elif "command prompt" in app_name or "cmd" in app_name:
        os.system("start cmd")
        speak("कमांड प्रॉम्प्ट खोल रहा हूँ।")
    else:
        speak("मुझे यह एप्लिकेशन नहीं मिली।")

def open_website(website_name):
    urls = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "facebook": "https://www.facebook.com",
        "github": "https://www.github.com"
    }
    
    for key in urls:
        if key in website_name:
            webbrowser.open(urls[key])
            speak(f"{key} खोल रहा हूँ।")
            return
    
    speak("मुझे यह वेबसाइट नहीं मिली।")

def control_browser(command):
    if "स्क्रॉल डाउन" in command:
        pyautogui.scroll(-1000)
        speak("स्क्रॉल कर रहा हूँ।")
    elif "स्क्रॉल अप" in command:
        pyautogui.scroll(1000)
        speak("ऊपर स्क्रॉल कर रहा हूँ।")
    elif "क्लिक" in command:
        pyautogui.click()
        speak("क्लिक किया गया।")
    else:
        speak("यह एक अज्ञात ब्राउज़र कमांड है।")

# Main loop
speak("नमस्ते, मैं आपका सहायक हूँ। आप क्या करना चाहेंगे?")
while True:
    query = listen()
    if query:
        if "बंद करो" in query or "exit" in query:
            speak("अलविदा!" )
            break
        elif "खोलो" in query:
            open_application(query)
        elif "वेबसाइट" in query:
            open_website(query)
        elif "स्क्रॉल" in query or "क्लिक" in query:
            control_browser(query)
        else:
            speak("मुझे यह कमांड समझ नहीं आई।")
