from datetime import datetime
from unittest import result
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    """
        function should speak the provided text
    """
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    """
        function should greet according to the time
    """
    hour = int(datetime.now().hour)
    
    if (hour>=0) and (hour < 12):
        speak("Good Morning")
    elif (hour >= 12) and (hour < 18):
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am jarvis sir, Please tell me how may I help you?")


def take_command():
    """
        It takes microphone input from the user and returns string output
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognzing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def send_email(content, to):
    """
        yet to implement
    """
    pass

if __name__ == "__main__":
    wish_me()
    
    while True:
        query = take_command().lower()

        if 'wikipedia' in query:
            speak("Seaching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(f"According to wikipedia {results}")
        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://google.co.in")

        elif 'open stackoverflow' in query:
            webbrowser.open("htts://stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'the time' in query:
            str_time = datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {str_time}")
        
        elif 'open code' in query:
            code_path = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
        
        elif 'email to faisal' in query:
            try:
                speak("What should I say?")
                content = take_command()
                to = "ansarifaisal480@gmail.com"
                send_email(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print("I am unable to send the mail")
        elif 'jarvis quit' in query:
            speak("Quitting sir, Thank you for your time")
            exit()