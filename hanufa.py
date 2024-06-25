import random
import bs4
import time
import pyttsx3
import speech_recognition as sr
import datetime #built in function
import wikipedia
import webbrowser #built in function
import os #built in function
import smtplib #built in function
import pywhatkit as kit
import subprocess as sp #built in function
import winsound
from playsound import playsound
import requests
from bs4 import BeautifulSoup
import pyautogui
import pyjokes

Websites={
    "stackoverflow":"https://stackoverflow.com/",
    "netflix":"https://netflix.com/",
    "disney":"https://hotstar.com/",
    "jio cinema":"https://hotstar.com/",
    "prime":"https://prime.com",
    "gmail":"https://gmail.com/"
}

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Hello Sir.....Very Good Morning")

    elif hour>=12 and hour<18:
        speak("Hello Sir....Good Afternoon")

    else:
        speak("Good Evening!")

    speak(" Jarvis is here to help you!")
    print('__________________________________________________________________________________________________________________________________________')
def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("Listening........")
        r.pause_threshold=0.5
        audio = r.listen(source)
    try:
        print(" ")
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.
        return query
    except Exception as e:
        print(e)    
    return query

def OpenWebsite(query):
    webt = list(Websites.keys())
    if any(i in query for i in webt):
        titles=[i for i in webt if i in query]
        for title in titles:
            webbrowser.open_new_tab(Websites[title])
        return "Opening {} website.".format(titles),1
    else:
        return "website not found"

def OpenApps(query):
    query=str(query).replace("open","").lower()
    pyautogui.hotkey("winleft")
    pyautogui.typewrite(query,0.2)
    time.sleep(0.5)
    pyautogui.hotkey("enter")

def jokes():
    c=['neutral','chuck','all','twister']
    catgo = random.choice(c)
    return pyjokes.get_joke(category=catgo)

def play_on_youtube(video):
    kit.playonyt(video)
    exit()
def search_on_google(query):
    res=kit.search(query)
    exit()
def alarm(Timing):
        Diff = str(datetime.datetime.now().strptime(Timing,"%I:%M %p"))
        Diff = Diff[11:-3]
        print(Diff)
        Horeal = Diff[:2]
        Horeal = int(Horeal)
        Mireal = Diff[3:5]
        Mireal = int(Mireal)
        print(f"Done, alarm is set for {Timing}")

        while True:
            if Horeal==datetime.datetime.now().hour:
                if Mireal==datetime.datetime.now().minute:
                    print("alarm is running")
                    winsound.PlaySound('abc',winsound.SND_LOOP)
                elif Mireal<datetime.datetime.now().minute:
                    break
def remainder(Timing,speak,text):
        Diff = str(datetime.datetime.now().strptime(Timing,"%I:%M %p"))
        Diff = Diff[11:-3]
        print(Diff)
        Horeal = Diff[:2]
        Horeal = int(Horeal)
        Mireal = Diff[3:5]
        Mireal = int(Mireal)
        speak("Done, Reminder set successfully for! {rem} at {Timing}")
        print(f"Done, Reminder set successfully for! {rem} at {Timing}")
        ennisarlu = 7
        count = 0
        while True:
            if Horeal==datetime.datetime.now().hour:
                if Mireal==datetime.datetime.now().minute:
                    speak(text)
                    count+=1
                if count==ennisarlu:
                    break
def Google_lies(query):
    base_url = "https://google.com/search?q="
    url = base_url+query
    requests_result=requests.get(url)
    soup=bs4.BeautifulSoup(requests_result.text,"html.parser")
    ans = soup.find("div",class_="BNeawe").text
    return ans
def Weather(query):
    temp=Google_lies(query)
    return temp

if __name__ =="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results=wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            speak('What do you want to play on Youtube, sir?')
            video = takeCommand().lower()
            play_on_youtube(video)

        elif 'search on google' in query:
            speak('What do you want to search on Google, sir?')
            query = takeCommand().lower()
            speak("Here are the results sir!")
            search_on_google(query)

        elif 'music' in query:
            music_dir = "C:\\Users\\Nazeer Mastan\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            speak('enjoy the music boss!')
            os.startfile(os.path.join(music_dir, songs[2]))
            exit()

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Boss, the time is {strTime}")

        elif 'how are you' in query:
            speak('I am fine Nazeer, how about you?')

        elif 'alarm' in query:
            speak("Yes Boss!, Please tell me time for example 5:30 A.M")
            tt = takeCommand()
            tt = tt.replace("set alarm to ", "")
            tt = tt.replace(".","")
            tt = tt.upper()
            alarm(tt)

        elif 'temperature' in query:
            english=[" at "," in "," of "," on "]
            if any(i in query for i in english):
                speak(Weather(query))
            else:
                speak("Of which city you want to know the weather?")
                place = takeCommand()
                speak(Weather("What is the current weather of"+place))

        elif 'set reminder' in query or 'reminder' in query:
            speak("Yes Boss! Can you please mention the time?")
            Timing = takeCommand()
            Timing = str(Timing).replace(".","")
            Timing = Timing.upper()
            speak("Time noted! Can you mention remainder?")
            rem=takeCommand()
            remainder(Timing,speak,rem)

        elif "website" in query:
            x=OpenWebsite(query)
            speak(x)
        elif "open" in query:
            y=OpenApps(query)

        elif "joke" in query:
            speak("There no any joke bigger than your existance my friend!, Even though I will tell you a joke")
            time.sleep(0.2)
            speak(jokes())
            print(jokes())

        elif 'quit' in query:
            speak('Quitting Boss')
            exit()