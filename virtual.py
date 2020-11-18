
# coding: utf-8

# In[2]:

import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
from ecapture import ecapture as ec
import smtplib
import time
import subprocess

print('Loading your AI personal assistant - Shivam Kumar')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning Shivam Kumar , How are you ?")
        print("Hello,Good Morning Shivam Kumar , How are you ?")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon Shivam Kumar , How are you ?")
        print("Hello,Good Afternoon Shivam Kumar , How are you ?")
    else:
        speak("Hello,Good Evening Shivam Kumar , How are you ?")
        print("Hello,Good Evening Shivam Kumar , How are you ?")
        

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kartik19agarwal@gmail.com', 'kartik1919')
    server.sendmail('kartik19agarwal@gmail.com', to, content)
    server.close()
        
        
        
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Tell me how can I help you now?")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        statement = r.recognize_google(audio, language='en-in')
        print(f"User said: {statement}\n")

    except Exception as e:
        print(e)    
        print("I'm sorry please say that again please...")  
        return "None"
    return statement

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        statement = takeCommand().lower()
        
        # Logic for executing tasks based on statement
        if "good bye" in statement or "ok bye" in statement or "quit" in statement or "stop" in statement:
            speak('your personal assistant Jarvis is shutting down,Good bye')
            print('your personal assistant Jarvis is shutting down,Good bye')
            break
            
            

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=4)
            speak("According to Wikipedia")
            print(results)
            speak(results)

            
        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)
            
        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
            
        elif 'mail' in statement:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "kumar.shivam0611@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend shivam. I am not able to send this email")   
            
        elif 'play music' in statement:
            music_dir = 'F:\music pc'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Jarvis Assistant version 1 point O your persoanl assistant. I am programmed by shivam to do minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia questions too!')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Shivam kumar")
            print("I was built by Shivam kumar")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif "camera" in statement or "take a photo" or "selfie" in statement:
            ec.capture(0,"spy_camera","selfie.jpg")
            
        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)


# In[ ]:



