import smtplib
from time import sleep

import pyttsx3
import datetime
import speech_recognition as sr
import sounddevice as sd
import numpy as np
import time
import wikipedia
import webbrowser
import os
import platform
import subprocess
import random
import pyautogui
import psutil
import pyjokes

# ---------- INIT TTS ENGINE ----------
engine = pyttsx3.init('nsss')  # macOS driver
engine.setProperty('rate', 170)

# Pick Alex voice if available
for v in engine.getProperty('voices'):
    if "Alex" in v.name:
        engine.setProperty('voice', v.id)
        break

# ---------- GLOBAL ----------
is_speaking = False
awake = False   # Jarvis is asleep until "hey jarvis"

# ---------- SPEAK ----------
def speak(text: str):
    global is_speaking
    is_speaking = True
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.5)
    is_speaking = False

# ---------- FEATURES ----------
def say_time():
    now = datetime.datetime.now()
    speak(f"The time is {now.strftime('%I:%M %p')}")

def say_date():
    now = datetime.datetime.now()
    speak(f"Today's date is {now.day} {now.strftime('%B')} {now.year}")

def greet():
    now = datetime.datetime.now()
    hour = now.hour
    if 6 <= hour < 12:
        wish = "Good morning sir."
    elif 12 <= hour < 16:
        wish = "Good afternoon sir."
    elif 16 <= hour < 19:
        wish = "Good evening sir."
    else:
        wish = "Good night sir."
    speak(f"Hello sir, {wish} What can I do for you?")

def exit_jarvis():
    speak("Goodbye sir. Going to sleep now.")
    time.sleep(2)
    raise SystemExit

def SendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('nomail@gmail.com', '123456')  # <-- replace with real creds
    server.sendmail('send@gmail.com', to, content)
    server.quit()

# ---------- LISTEN ----------
def commandlistening(duration=3):
    """Listen once and return recognized text"""
    if is_speaking:
        return ""

    r = sr.Recognizer()
    r.pause_threshold = 0.8
    samplerate = 16000

    try:
        audio_data = sd.rec(int(duration * samplerate),
                            samplerate=samplerate,
                            channels=1,
                            dtype='int16')
        sd.wait()

        audio = sr.AudioData(
            np.array(audio_data, dtype=np.int16).tobytes(),
            samplerate,
            2
        )

        query = r.recognize_google(audio, language='en-IN')
        print("You said:", query)
        return query.lower().strip()

    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        speak("Sorry, sir. Google services are down.")
        return ""

# ---------- SCREENSHOT FEATURE ----------
def screenshot():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"/Users/apple/Desktop/aamir/coding/python/Ai with udemy/screenshot_{timestamp}.png"
    img = pyautogui.screenshot()
    img.save(filename)
    speak(f"Screenshot saved as {filename}")

# ---------- SYSTEM STATUS ----------
def cpu():
    usage = psutil.cpu_percent()
    engine.say(f"CPU usage is {usage} percent")
    print(f"jarvis: cpu usege is {usage} percent")

    time.sleep(3)

    battery = psutil.sensors_battery()
    if battery:
        speak(f"Battery is at {battery.percent} percent")
    else:
        speak("Battery information is not available")

def jokes():
    joke = pyjokes.get_joke(language="en", category="neutral")
    speak(joke)
    time.sleep(10)

# ---------- MAIN ----------
if __name__ == "__main__":
    speak("Jarvis is now online. Say 'Hey Jarvis' to wake me up.")

    while True:
        query = commandlistening(duration=5)
        if not query:
            continue

        # --- WAKE WORD ---
        if not awake and ("hey jarvis" in query or "jarvis" in query):
            awake = True
            greet()
            continue

        if awake:
            if "time" in query:
                say_time()

            elif "date" in query:
                say_date()

            elif "greet" in query or "wish" in query or "wish me" in query:
                greet()

            elif "wow" in query:
                speak("Thanks for your wow")

            elif "screenshot" in query:
                screenshot()

            elif "wikipedia" in query:
                try:
                    speak("Searching Wikipedia...")
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    print(results)
                    speak(results)
                except wikipedia.DisambiguationError:
                    speak("Your query is too broad. Please be more specific.")
                except wikipedia.PageError:
                    speak("Sorry, I could not find anything on Wikipedia.")

            elif "google" in query:
                q = query.replace("google", "").strip()
                if q:
                    speak(f"Searching Google for {q}")
                    webbrowser.open(f"https://www.google.com/search?q={q}")
                else:
                    speak("What should I search on Google?")

            elif "email" in query or "mail" in query:
                try:
                    speak("What should I say?")
                    content = commandlistening()
                    to = "xyz@gmail.com"
                    # SendEmail(to, content)  # uncomment to use
                    speak(content)
                    speak("Email sent successfully")
                except Exception as e:
                    print(e)
                    speak("Unable to send email")

            elif "logout" in query:
                if platform.system() == "Windows":
                    os.system("shutdown -l")
                else:
                    os.system("osascript -e 'tell application \"System Events\" to log out'")

            elif "shutdown" in query:
                if platform.system() == "Windows":
                    os.system("shutdown /s /t 1")
                else:
                    os.system("osascript -e 'tell application \"System Events\" to shut down'")

            elif "restart" in query:
                if platform.system() == "Windows":
                    os.system("shutdown /r /t 1")
                else:
                    os.system("osascript -e 'tell application \"System Events\" to restart'")

            elif "play music" in query or "play song" in query:
                songs_dir = "/Users/apple/Downloads"
                songs = os.listdir(songs_dir)
                songs = [f for f in songs if f.endswith(('.mp3', '.wav', '.m4a'))]

                if songs:
                    song_path = os.path.join(songs_dir, songs[0])
                    subprocess.call(['open', song_path])
                else:
                    speak("No songs found in the folder.")

            elif "stop music" in query or "close music" in query:
                os.system("pkill -9 Music")
                os.system("pkill -9 QuickTime Player")
                os.system("pkill -9 VLC")

            elif "cpu" in query or "compute performance" in query or "battery" in query:
                cpu()

            elif "do you remember that" in query or "do you remember" in query:
                try:
                    with open("data.txt", "r") as remember:
                        memory = remember.read().strip()
                        if memory:
                            speak("You asked me to remember: " + memory)
                        else:
                            speak("I don’t have anything remembered yet.")
                except FileNotFoundError:
                    speak("I don’t have anything remembered yet.")

            elif "remember that" in query or "remember" in query:
                speak("What should I remember?")
                data = commandlistening().strip()
                if data:
                    speak("Okay, I will remember: " + data)
                    with open("data.txt", "w") as remember:
                        remember.write(data)
                else:
                    speak("I didn’t catch that. Please say it again.")

            elif 'jokes' in query or "joke" in query:
                jokes()

            elif any(word in query for word in ["stop", "exit", "quit", "close"]):
                exit_jarvis()

            elif "sleep" in query:
                engine.say("Okay sir, I am going back to sleep. Say 'Hey Jarvis' to wake me again.")
                awake = False
