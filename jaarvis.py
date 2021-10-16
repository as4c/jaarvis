import subprocess
from urllib.request import urlopen
import pyttsx3
import speech_recognition as sr
from datetime import datetime 
import wikipedia
import webbrowser
import os
import smtplib
import pyjokes
import pyautogui
import random
import json
import time
import ctypes
from wikipedia import exceptions
import requests
import pickle
import wolframalpha
from twilio.rest import Client
import winshell








engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)
# print(voices[0])--> for male voice
# print(voices[1])--> for female voice


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

def clear():
    clear=lambda:os.system('cls')
if __name__=="__main__":
    # lambda:os.system('cls')
    clear() 
    WishMe()
    speak("I'M Jaarvis, Tell me how can I help you!")       

    while True:
    # if 1:
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

            webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open("http://google.com")
            speak("Sir Google Chrome opened")
        

        elif " search" in query:
            speak("Sir what do you want to search")
            search=takecommand(1).lower()
            search_url = (f"https://www.google.com/search?q={search}")
            webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open(search_url)

        elif "play music" in query or  "gaana bajao" in query:
        # elif "gaana bajao" in query:
               music_dir="D:\\As music\\Music files"
               songs=os.listdir(music_dir)
               print(songs)
               os.startfile(os.path.join(music_dir,songs[2]))
            #    os.startfile(random.choice(songs))

        elif 'the time' in query:
            strTime=datetime.now().strftime("%H : %M : %S")
            speak(f"Sir the time is {strTime}")

        elif ' the date ' in query:
            
            strTime=datetime.today().strftime("%B %d, %Y")
            # print(Today)
            speak(f"sir today is {strTime}")

        elif ' open code' in query:
            codePath=r"C:\\Users\\SAGAR\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)


        elif 'send email to friend1' in query:
            try:
                speak("What should I Say?")
                content=takecommand(1).lower()
                
                to = "addghh@gmail.com"

                
                sendEmail(to,content)
                speak("Sir Email has been sent to shivam!")
            except Exception as e:
                print(e)
                speak("sorry sam I am not able to sent email!")
        elif 'send email to friend2' in query:
            try:
                speak("What should I Say?")
                content=takecommand(1).lower()
                to="asdflkjghmnbvcxzp@gmail.com"
                sendEmail(to,content)
                speak("Sir Email has been sent to Amit!")
            except Exception as e:
                print(e)
                speak("sorry sam I am not able to sent email!")
        elif 'send a mail' in query:
            try:
                speak("whome should you send email:")
                takecommand(1).lower()
                speak("What should you Say?")
                content=takecommand(1).lower()
                to = takecommand(1).lower()
                sendEmail(to,content)
                speak("Sir Email has been sent to sagar!")
            except Exception as e:
                print(e)
                speak("sorry sam I am not able to sent email!")
        
        elif 'send email to friend3' in query:
            try:
                speak("What should I Say?")
                content=takecommand(1).lower()
                #

                to = "*&^^%$##@gmail.com"
                sendEmail(to,content)
                speak("Sir Email has been sent to nikhil!")
            except Exception as e:
                print(e)
                speak("sorry sam I am not able to sent email!")
        
        elif "joke" in query:
            speak("Searching jokes")
            joke=pyjokes.get_joke()
            print(joke)
            speak(joke)
        
        elif "take screenshot" in query:
            image=pyautogui.screenshot()
            image.save("screenshots.png")
            speak("Sir screenshot Taken")


        elif "how are you" in query:
            speak("I'M Fine,Thankyou")
            speak("How are you sir")

        elif "fine" in query :
            # or"Good" in query
            speak("It's good to know that you are fine")
        
        elif "what's your name" in query  or "What is your name" in query:
            speak("My friends call me sagar")

        elif "who made you"  in query or "who created you" in query:
            speak("I Have Been created by Avengers")
        
        elif "news" in query:
                url=('https://newsapi.org//v2//top-headlines?''country = in&' 'apiKey = ')
                url +='your_api_key_here'
                try:
                    Response = requests.get(url)
                except:
                    speak("can,t access link, plz check you internet ")
  
                news = json.loads(Response.text)
  
  
                for new in news['articles']:
                    print("##############################################################\n")
                    print(str(new['title']), "\n\n")
                    speak(str(new['title']))
                    print('______________________________________________________\n')
  
   
  
                    print(str(new['description']), "\n\n")
                    speak(str(new['description']))
            
                    print("..............................................................")
                    time.sleep(2)
                # data = json.load(jsonObj)
                # i=1

                # speak('here are some top news from the times of india')
                # print('=============== TIMES OF INDIA ============'+ '\n')

            #     for item in data['article']:

            #         print(str(i) + '. ' + item['title'])
            #         print(item['description'] + '\n')
            #         speak(str(i) + '. ' + item['title'])
            #         i +=1
            # except Exception as e:
            #     print(e)
        elif "lock window" in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif "shutdown system" in query:
            speak("Hold On a sec! your system is on its way to shutdown ")
            subprocess.call("shutdown / p /f")
        
        elif "restart " in query:
            speak("restarting your computer!")
            subprocess.call(["shutdown","/r"])
        
        elif "log off" in query or "sign out" in query:
            time.sleep(5) 
            subprocess.call(["shutdown","/l"])

        elif "don't listen" in query:
            speak("For how much time you want to stop me sir")
            a=int(takecommand(1))
            time.sleep(a)
            print(a)

        elif "exit" in query:
            speak("Thanks for giving me your time:")
            exit()
            
        elif "calculate" in query:
            app_id = "Wolframalpha api id"
                        # clnt= wolframalpha.Client(app_id)
                        # indx = query.lower().split().index('calculate')
                        # query = query.split()[indx + 1:]
                        # res = clnt.query(' '.join(query)) 
                     
                     
                        # answer = next(res.results).text
                        # print("The answer is " + answer)
                        # speak("The answer is " + answer)
        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
													0,
													"Location of wallpaper",
													0)
            speak("Background changed successfully")
        
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")

        # elif "camera" in query or "take a photo" in query:
            # ec.capture(0, "Jarvis Camera ", "img.jpg")
        elif "weather" in query:
            	# Google Open weather website
			    # to get API of Open weather
            api_key = "Api key"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ")
            print("City name : ")
            city_name = takecommand(1)
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
                speak(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
            else:
                    speak(" City Not Found ")
            
        elif "make notes" in query:
            speak("What should i write, sir")
            note = takecommand(1)
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takecommand(1)
            if 'sure' in snfm:
                strTime=datetime.now().strftime("%H : %M : %S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
        elif "show my notes" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")  
            print(file.read())
            speak(file.read(6))
        
