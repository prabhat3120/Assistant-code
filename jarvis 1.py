import sys
import speech_recognition as sr
import os
import webbrowser
import time
import pyttsx3  # Voice Output के लिए
# import openai 
# Terminal में हिंदी टेक्स्ट सही दिखाने के लिए
sys.stdout.reconfigure(encoding='utf-8')

# Speech Engine को Initialize करना
engine = pyttsx3.init()

# आवाज़ की सेटिंग (Jarvis जैसी Male Voice)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Male voice: voices[0], Female voice: voices[1]
engine.setProperty('rate', 175)  # बोलने की स्पीड (Default: 200, Adjust as needed)
engine.setProperty('volume', 1.0)  # आवाज़ की लाउडनेस

# Text-to-Speech Function
def speak(text):
    print("AI Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Voice Command सुनने का Function
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("सुन रहा हूँ... कृपया बोलें।")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio, language="hi-IN")
        print("आपने कहा:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("मुझे आपकी आवाज़ समझ नहीं आई, कृपया फिर से बोलें।")
        return ""
    except sr.RequestError:
        speak("सर्वर से कनेक्ट नहीं हो पाया, कृपया इंटरनेट जांचें।")
        return ""

# Command को Process करने का Function
def process_command(command):
    if "क्रोम खोलो" in command:
        speak("क्रोम खोल रहा हूँ।")
        webbrowser.open("https://www.google.com")

    elif "नोटपैड खोलो" in command:
        speak("नोटपैड खोल रहा हूँ।")
        os.system("notepad")

    elif "कैलकुलेटर खोलो" in command:
        speak("कैलकुलेटर खोल रहा हूँ।")
        os.system("calc")

    elif "यूट्यूब पर गाना चलाओ" in command:
        speak("आप कौन सा गाना सुनना चाहते हैं?")
        song = listen()
        if song:
            speak(f"यूट्यूब पर {song} खोज रहा हूँ।")
            webbrowser.open(f"https://www.youtube.com/results?search_query={song}")

    elif "वेबसाइट खोलो" in command:
        speak("कौन सी वेबसाइट खोलनी है?")
        site = listen()
        if site:
            speak(f"{site} खोल रहा हूँ।")
            webbrowser.open(f"https://{site}.com")

    elif "गूगल पर खोजो" in command:
        speak("आप क्या खोजना चाहते हैं?")
        query = listen()
        if query:
            speak(f"गूगल पर {query} खोज रहा हूँ।")
            webbrowser.open(f"https://www.google.com/search?q={query}")

    elif "बंद हो जाओ" in command or "exit" in command:
        speak("अलविदा, आपका दिन शुभ हो।")
        exit()
    
    else:
        speak("मुझे यह कमांड समझ नहीं आई, मैं इसे गूगल पर खोज रहा हूँ।")
        webbrowser.open(f"https://www.google.com/search?q={command}")

# Main Function
def main():
    speak("नमस्ते, मैं आपका स्मार्ट असिस्टेंट हूँ।")
    while True:
        command = listen()
        if command:
            process_command(command)
        time.sleep(1)

if __name__ == "__main__":
    main()