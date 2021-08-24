import pyttsx3
import os
from tkinter import *
import speech_recognition as sr
import webbrowser
import datetime
import subprocess
import wikipedia
from PIL import ImageTk, Image

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        lisvar.set("Listening...")
        tkWindow.update()
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            lisvar.set("Recognizing...")
            tkWindow.update()
            Query = r.recognize_google(audio, language='en-in')
            print("the command is printed=", Query)
         

        except Exception as e:
            print(e)
            lisvar.set("Can you repeat that")
            return "None"
        user_said.set(Query)
        tkWindow.update()
        return Query


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def tellDay():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        lisvar.set("The day is " + day_of_the_week)
        speak("The day is " + day_of_the_week)


def tellTime():
    time = str(datetime.datetime.now())
    hour = time[11:13]
    min = time[14:16]
    lisvar.set("The time is " + hour + " Hours and " + min + " Minutes")
    speak("The time is" + hour + "Hours and" + min + "Minutes")

def Take_query():
    query = takeCommand().lower()
    if 'exit' in query:
        lisvar.set("Good bye")
        tkWindow.update()
        speak("Good bye")
        exit()

    elif "wikipedia" in query:
        if "open wikipedia" in query:
            webbrowser.open('wikipedia.com')
        else:
            try:
                speak("Searching wikipedia ")
                query = query.replace("according to wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                lisvar.set(result)
                tkWindow.update()
                speak(result)
            except Exception as e:
                lisvar.set("Sorry sir could not find any results")
                tkWindow.update()
                speak("Sorry sir could not find any results")

    elif "open youtube" in query:
        lisvar.set("Here you go to Youtube")
        tkWindow.update()
        speak("Here you go to Youtube")
        webbrowser.open("https://www.youtube.com/")

    elif "open drive" in query:
        lisvar.set("Opening Drive")
        tkWindow.update()
        speak("Opening Drive")
        webbrowser.open("http://gdrivephp.epizy.com/")

    elif "open google" in query:
        lisvar.set("Opening Google")
        tkWindow.update()
        speak("Opening Google")
        webbrowser.open("www.google.com")

    elif "open stack overflow" in query:
        lisvar.set("Here you go to Stack Over flow.Happy coding")
        tkWindow.update()
        speak("Here you go to Stack Over flow.Happy coding")
        webbrowser.open("https://stackoverflow.com/")


    elif "shutdown system" in query:
        lisvar.set("The system is shutting down")
        tkWindow.update()
        speak("The system is shutting down")
        subprocess.call('shutdown / p /f')

    elif "restart" in query:
        lisvar.set("The system is restarting")
        tkWindow.update()
        speak("The system is restarting")
        subprocess.call(["shutdown", "/r"])

    elif "hibernate" in query or "sleep" in query:
        lisvar.set("The system is on sleep")
        tkWindow.update()
        speak("The system is on sleep")
        subprocess.call("shutdown / h")

    elif "which day it is" in query:
        tellDay()

    elif "tell me the time" in query:
        tellTime()

    elif "tell me your name" in query:
        lisvar.set("I am Your deskstop Assistant")
        speak("I am Your deskstop Assistant")

if __name__ == '__main__':
    tkWindow = Tk()
    tkWindow.title("Virtual Assistant")
    tkWindow.wm_iconbitmap("micicon1.ico")
    tkWindow.geometry('500x600')

    ftop = Frame(tkWindow, bg='#B5B1B1')  

    user_saiddefault = StringVar()
    userlabel1 = Label(ftop, textvariable=user_saiddefault, font="Century 14 normal", fg='black', bg='#B5B1B1')
    user_saiddefault.set("User Said:")
    userlabel1.place(x=20, y=20, width=100, height=30)
 
    user_said = StringVar()
    userlabel = Label(ftop, textvariable=user_said, font="Century 14 normal", fg='black', bg='#B5B1B1')
    userlabel.place(x=120, y=20, width=220, height=30)

    ftop.place(x=0, y=0, width=500, height=100)

    f1 = Frame(tkWindow, bg='#B5b1b1')  

    image = Image.open('Mic.png')
    image = image.resize((210, 200), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(image)

    button = Button(f1, image=img1, bg='#B5b1b1', border='0', cursor='hand2', command=Take_query)
    button.pack()
   
    lisvar = StringVar()
    lis = Label(f1, textvariable=lisvar, font="Century 15 normal", bg='#B5b1b1', fg='black', wraplength=500,
                justify='center')  
    lisvar.set("Welcome")

    lis.pack(pady=30)

    f1.place(x=0, y=100, width=500, height=500)

    tkWindow.resizable(0, 0)
    tkWindow.mainloop()


