import pyttsx3
import pywin32_system32
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random
import pyautogui
import pyjokes #instal pyjokes
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    print("The current time is ", Time)

def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)
    print("The current date is " + str(day) + "/" + str(month) + "/" + str(year))

def wishme():
    print("Welcome back sir!!")
    speak("Welcome back sir!!")
    
    hour = datetime.datetime.now().hour
    if hour >= 4 and hour < 12:
        speak("Good Morning Sir!!")
        print("Good Morning Sir!!")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon Sir!!")
        print("Good Afternoon Sir!!")
    elif hour >= 16 and hour < 24:
        speak("Good Evening Sir!!")
        print("Good Evening Sir!!")
    else:
        speak("Good Night Sir, See You Tommorrow")

    speak("Rahul at your service sir, please tell me how may I help you.")
    print("Rahul at your service sir, please tell me how may I help you.")

def screenshot():
    img = pyautogui.screenshot()
    img.save("D:\\jarvish_image\\js.png")

def jokes():
    my_joke = pyjokes.get_joke('en',category='neutral')
    print(my_joke)
    speak(my_joke)

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)

    except Exception as e:
        print(e)
        speak("Please say that again")
        return "Try Again"

    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "who are you" in query:
            speak("I'm Rahul created by Mr. Rahul and I'm a desktop voice assistant.")
            print("I'm Rahul created by Mr. Rahul and I'm a desktop voice assistant.")

        elif "how are you" in query:
            speak("I'm fine sir, What about you?")
            print("I'm fine sir, What about you?")

        elif "fine" in query:
            speak("Glad to hear that sir!!")
            print("Glad to hear that sir!!")

        elif "good" in query:
            speak("Glad to hear that sir!!")
            print("Glad to hear that sir!!")

        elif "wikipedia" in query:
            try:
                speak("Ok wait sir, I'm searching...")
                query = query.replace("wikipedia","")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            except:
                speak("Can't find this page sir, please ask something else")
        
        elif "open youtube" in query:
            wb.open("youtube.com") 

        elif "open google" in query:
            wb.open("google.com") 
   
        elif "open gate overflow" in query:
            wb.open("gateoverflow.com")

        elif "cricket score" in query:
            wb.open("Cricbuzz.com")

        elif "play music" in query:
            music = "D:\\music"
            songs = os.listdir(music)
            print(songs)
            x = len(songs)
            y = random.randint(0,x)
            os.startfile(os.path.join(music,songs[y]))

        elif "open chrome" in query:
            chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\chrome.exe'
            os.startfile(chromePath)
           
            
        elif "screenshot" in query:
            screenshot()
            speak("I've taken screenshot, please check it")
            print("I've taken screenshot, please check it")
         
        elif "joke" in query:

            jokes()

        elif "offline" in query:

            speak("Rahul goes shut down,Bye sir")
            print ("Rahul goes shut down,Bye sir")
            quit()

