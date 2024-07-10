import streamlit as st
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyautogui

def speak(var):
    tts = pyttsx3.init()
    tts.say(var)
    tts.runAndWait()

def wish():
    time_ = datetime.datetime.now().hour
    if 0 <= time_ < 12:
        speak("Good Morning Sasank")
    elif 12 <= time_ < 16:
        speak("Good Afternoon Sasank")
    else:
        speak("Good Evening Sasank")
    speak("How can I help you")

def sprec():
    rec = sr.Recognizer()
    rec.pause_threshold = 1
    with sr.Microphone() as roh:
        st.write("Listening...")
        aud = rec.listen(roh)
    try:
        st.write("Recognizing...")
        query = rec.recognize_google(aud)
        query = query.lower()
        st.write(f"You said: {query}")
        return query
    except:
        st.write("Sorry, I didn't get that")
        speak("Sorry, I didn't get that")
        return None

def handle_query(global_query):
    if global_query:
        if "wikipedia" in global_query:
            speak("Searching on Wikipedia...")
            global_query = global_query.replace("wikipedia", "")
            output = wikipedia.summary(global_query, sentences=2)
            st.write(output)
            speak("According to Wikipedia")
            speak(output)
        elif "open" in global_query:
            global_query = global_query.replace("open", "")
            speak(f"Opening {global_query}")
            webbrowser.open(f"http://www.{global_query}.com")
        elif "the time" in global_query:
            hour = datetime.datetime.now().hour
            minute = datetime.datetime.now().minute
            speak(f"It's {hour} {minute}")
        elif "play music on spotify" in global_query:
            webbrowser.open_new("https://open.spotify.com/")
        elif "play music" in global_query or 'play songs' in global_query:
            songs = os.listdir("C:\\Users\\USER\\Music")
            os.startfile(os.path.join("C:\\Users\\USER\\Music", songs[1]))
        elif "launch vs code" in global_query or "launch visual studio code" in global_query:
            speak("Opening VS Code")
            os.startfile("C:\\Users\\USER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        elif "launch calculator" in global_query:
            speak("Opening Calculator")
            os.startfile('calc.exe')
        elif "google" in global_query:
            txt = global_query.replace("google", "").strip()
            webbrowser.open(f"http://www.google.com/search?q={txt}")
        elif "launch notepad" in global_query:
            speak("Opening Notepad")
            os.startfile('notepad.exe')
            speak("Do you want to type anything?")
            response = sprec()
            if response and ("yes" in response or "sure" in response):
                pyautogui.hotkey('win', 'h')
        elif "launch settings" in global_query:
            pyautogui.hotkey('win', 'i')
        elif "launch explorer" in global_query or "launch my computer" in global_query or "launch this pc" in global_query:
            pyautogui.hotkey('win', 'e')
        elif "launch task manager" in global_query:
            pyautogui.hotkey('ctrl', 'shift', 'escape')
        elif "who are you" in global_query or "what can you do" in global_query:
            speak("I am your virtual assistant. I can open apps, search for info, play music, and more. I am developed by Sasank.")
        elif "shutdown" in global_query:
            shutdown()

def shutdown():
    speak("Shutting down")
    st.stop()

def main():
    st.title("Virtual Assistant by Sasank")
    st.write("How can I help you?")
    
    if st.button("Run Assistant"):
        wish()
        global_query = sprec()
        handle_query(global_query)
    
    if st.button("Shut down"):
        shutdown()

if __name__ == "__main__":
    main()
