import streamlit as st
import pyttsx3
import datetime
import speech_recognition as sr
import wikipediaapi
import webbrowser
import os

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def wish():
    current_time = datetime.datetime.now().hour
    if 0 <= current_time < 12:
        speak("Good Morning")
    elif 12 <= current_time < 16:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("How can I help you?")

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = recognizer.listen(source)
    
    try:
        st.write("Recognizing...")
        query = recognizer.recognize_google(audio)
        query = query.lower()
        st.write(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        st.write("Sorry, I didn't get that")
        speak("Sorry, I didn't get that")
    except sr.RequestError:
        st.write("Sorry, I'm having trouble with my speech recognition")
        speak("Sorry, I'm having trouble with my speech recognition")

def handle_query(query):
    if query:
        wiki_wiki = wikipediaapi.Wikipedia('en')
        if "wikipedia" in query:
            speak("Searching on Wikipedia...")
            query = query.replace("wikipedia", "")
            page = wiki_wiki.page(query)
            if page.exists():
                summary = page.summary[:500]  # Limit summary to 500 characters
                st.write(summary)
                speak("According to Wikipedia")
                speak(summary)
            else:
                st.write("Wikipedia page not found")
                speak("Wikipedia page not found")
        elif "open" in query:
            query = query.replace("open", "")
            speak(f"Opening {query}")
            webbrowser.open(f"http://www.{query}.com")
        elif "the time" in query:
            current_time = datetime.datetime.now().strftime("%H:%M")
            st.write(f"It's {current_time}")
            speak(f"It's {current_time}")
        elif "play music" in query or 'play songs' in query:
            songs_dir = "C:\\Users\\USER\\Music"  # Replace with your music directory
            if os.path.exists(songs_dir):
                songs = os.listdir(songs_dir)
                if songs:
                    os.startfile(os.path.join(songs_dir, songs[0]))  # Play the first song
                else:
                    st.write("No music files found")
                    speak("No music files found")
            else:
                st.write("Music directory not found")
                speak("Music directory not found")
        elif "shutdown" in query:
            speak("Shutting down")
            st.stop()
        else:
            st.write("Command not recognized")
            speak("Command not recognized")

def main():
    st.title("Virtual Assistant")
    st.write("How can I assist you today?")

    if st.button("Run Assistant"):
        wish()
        query = recognize_speech()
        handle_query(query)

if __name__ == "__main__":
    main()
