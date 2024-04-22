import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Define functions for speaking and listening
def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
        return text.lower()
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None

# Main loop
while True:
    text = listen()
    if text:
        if "hello" in text or "hi" in text:
            speak("Hello! How can I help you today?")
        elif "time" in text:
            speak(datetime.datetime.now().strftime("%H:%M:%S"))
        elif "date" in text:
            speak(datetime.date.today().strftime("%Y-%m-%d"))
        elif "search" in text:
            search_term = text.split("search for ")[-1]
            webbrowser.open(f"https://www.google.com/search?q={search_term}")
            speak(f"Opening search results for '{search_term}'")
        else:
            speak("Sorry, I can't understand your command.")

print("Exiting...")