import pyttsx3
import speech_recognition as sr
from datetime import datetime 
import wikipedia
import webbrowser
import os
import smtplib





engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices)
engine.setProperty('voices',voices[0].id)
# print(voices[0])


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def WishMe():
    Hour=int(datetime.now().hour)
    if Hour>=0 and Hour<12:
        speak("Good Morning Sir!")
    elif Hour>=12 and Hour<17:
        speak("Good Afternoon Sir!")
    elif 17<=Hour<20:
        speak("Good Evening Sir")
    else:
        speak("Good Night Sir!")



def takecommand(__enter__):
    #it takes microphone input from user and return string output.
    r=sr.Recognizer()
    with sr.Microphone() as source:
        

        print("listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("as4avengersagar@gmail.com","*********")
    server.sendmail("as4avengersagar@gmail.com",to,content)
    server.close()
if __name__=="__main__": 
    WishMe()
    speak("I'M Jaarvis, Tell me how can I help you!")       

    # while True:
    if 1:
        query=takecommand(1).lower()
        #logic for executing tasks based on query
        if 'open wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia"," ")
            results=wikipedia.summary(query,sentences=5)
            speak("According to wikipedia")
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            speak(" Opening Youtube")
            # query=query.replace("youtube"," ")
            webbrowser.open("youtube.com")
            speak("Sir Youtube opened")
            query=query.replace("youtube"," ")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif "open chrome" in query:
            speak("Google chrome opening")
            # url = 'http://docs.python.org/'

            # chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://google.com")
            speak("Sir Google Chrome opened")
        

        elif " search" in query:
            speak("Sir what you want to search")
            search=takecommand(1).lower()
            webbrowser.get("search").open("http://google.com")

        elif "play music" in query:
        # elif "gaana bajao" in query:
               music_dir="D:\\As music\\Music files"
               songs=os.listdir(music_dir)
               print(songs)
               os.startfile(os.path.join(music_dir,songs[1]))
        elif 'the time' in query:
            strTime=datetime.now().strftime("%H : %M : %S")
            speak(f"Sir the time is {strTime}")

        elif ' the date ' in query:
            
            strTime=datetime.today().strftime("%B %d, %Y")
            # print(Today)
            speak(f"sir today is {strTime}")

        elif ' open code' in query:
            codePath="C:\\Users\\SAGAR\\AppData\\Local\\Programs\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'send email to shivam' in query:
            try:
                speak("What should I Say?")
                content=takecommand(1).lower()
                # to="amit8298030042@gmail.com"
                to = "shivamjhapali67@gmail.com"

                # to = "sagarkumarkhaira61@gmail.com"
                sendEmail(to,content)
                speak("Sir Email has been sent to shivam!")
            except Exception as e:
                print(e)
                speak("sorry sam I am not able to sent email!")
        elif 'send email to amit' in query:
            try:
                speak("What should I Say?")
                content=takecommand(1).lower()
                to="amit8298030042@gmail.com"
                sendEmail(to,content)
                speak("Sir Email has been sent to Amit!")
            except Exception as e:
                print(e)
                speak("sorry sam I am not able to sent email!")
        elif 'send email to me' in query:
            try:
                speak("What should I Say?")
                content=takecommand(1).lower()
                to = "sagarkumarkhaira61@gmail.com"
                sendEmail(to,content)
                speak("Sir Email has been sent to sagar!")
            except Exception as e:
                print(e)
                speak("sorry sam I am not able to sent email!")
        
        elif 'send email to nikhil' in query:
            try:
                speak("What should I Say?")
                content=takecommand(1).lower()
                # to="amit8298030042@gmail.com"
                # to = "shivamjhapali67@gmail.com"

                to = "kumarnikhil15700@gmail.com"
                sendEmail(to,content)
                speak("Sir Email has been sent to nikhil!")
            except Exception as e:
                print(e)
                speak("sorry sam I am not able to sent email!")