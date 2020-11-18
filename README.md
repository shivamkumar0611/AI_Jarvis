# shivamkumar0611 \( AI_Jarvis \)
<p align="center">
  <img src="https://github.com/shivamkumar0611/AI_Jarvis/blob/master/files/OfIQLs0uQD.png">
</p>
Created and Tested on Windows 10 with Python 3.6
An attempt to make a very simple, Personal Assistant that understands speech as well as text input and is capable of performing tasks other than conversing. This project is based on weak AI and this project does not implement any sort of machine learning or language processing. Combined with a few python scripts, J.A.R.V.I.S now performs quite a few tasks:
## Just goto AI_Jarvis/__pycache__/ and download virtualAI.cpython-36.pyc file in a new folder so that the pictures will be save in that folder only :)
That's all leave everything ...

# Imagine how easier it would be to send emails without typing a single word, doing Wikipedia searches without opening web browsers, and performing many other daily tasks like playing music with the help of a single voice command.

# What can this A.I. assistant do for you?
It can send emails for you.
It can play music for you.
It can do Wikipedia searches for you.
It is capable of opening websites like Google, Youtube, etc., in a web browser.

# Starting VS Code
I am going to use jupyter notebook you can use the VS Code IDE. Feel free to use any other IDE you are comfortable with. Start a new project and make a file called virtual.py.

Defining Speak Function
The first and foremost thing for an A.I. assistant is that it should be able to speak. To make our J.A.R.V.I.S. talk, we will make a function called speak(). This function will take audio as an argument, and then, it will pronounce it.

def speak(audio):
       pass      #For now, we will write the conditions later.
Now, the next thing we need is audio. We must supply audio so that we can pronounce it using the speak() function we made. We are going to install a module called pyttsx3.

What is pyttsx3?
A python library which will help us to convert text to speech. In short, it is a text-to-speech library.
It works offline, and it is compatible with Python 2 as well the Python 3.
Installation:

pip install pyttsx3
In case you receive such errors: 

No module named win32com.client
No module named win32
No module named win32api
Then, install pypiwin32 by typing the below command in the terminal :

pip install pypiwin32.
After successfully installing pyttsx3, import this module in your program.

Usage:

import pyttsx3
engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voice[0].id)

# What is sapi5?
Speech API developed by Microsoft.
Helps in synthesis and recognition of voice.
What Is VoiceId?
Voice id helps us to select different voices.
voice[0].id = Male voice 
voice[1].id = Female voice

# Writing Our speak() Function :
We made a function called speak() at the starting of this tutorial. Now, we will write our speak() function so that it can convert our text to speech.

def speak(audio):
engine.say(audio) 
engine.runAndWait() #Without this command, speech will not be audible to us.

# Creating Our main() function: 
Now, we will create a main() function, and inside this main() Function, we will call our speak function.

Code:
if __name__ == "__main__":
    wishMe()
Whatever you will write inside this speak() function will be converted into speech. Congratulations! With this, our J.A.R.V.I.S. has its own voice, and it is ready to speak.

# Defining Take command Function :
The next most important thing for our A.I. assistant is that it should be able to take command with the help of the microphone of the user's system. So, now we will make a takeCommand() function.  With the help of the takeCommand() function, our A.I. assistant will be able to return a string output by taking microphone input from the user.

# Before defining the takeCommand() function, we need to install a module called speechRecognition. Install this module by: 
pip install speechRecognition
After successfully installing this module, import this module into the program by writing an import statement.
import speechRecognition as sr

# Let's start coding the takeCommand() function :
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

 We have successfully created our takeCommand() function. Now we are going to add a try and except block to our program to handle errors effectively.
     try:
        print("Recognizing...")
        statement = r.recognize_google(audio, language='en-in')
        print(f"User said: {statement}\n")

    except Exception as e:
        print(e)    
        print("I'm sorry please say that again please...")  
        return "None"
    return statement

# Defining Task 1: To search something on Wikipedia 
 pip install wikipedia 
 
         if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=4)
            speak("According to Wikipedia")
            print(results)
            speak(results)
# Defining Task 2: To open YouTube site , mail,google , see current time 
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
            
# Defining Task 3: To play music
        elif 'play music' in statement:
            music_dir = 'F:\music pc'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

# Defining Task 7: To send Email
To send an email, we need to import a module called smtplib.

What is smtplib?

Simple Mail Transfer Protocol (SMTP) is a protocol that allows us to send emails and to route emails between mail servers. An instance method called sendmail is present in the SMTP module. This instance method allows us to send an email.  It takes 3 parameters:
The sender: Email address of the sender.
The receiver:T Email of the receiver.
The message: A string message which needs to be sent to one or more than one recipient.

# Defining Send email function :
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
In the above code, we are using the SMTP module, which we have already discussed above.

Note: Do not forget to 'enable the less secure apps' feature in your Gmail account. Otherwise, the sendEmail function will not work properly.

# Calling sendEmail() function inside the main() function:  
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
                
# Recapitulate
1. First of all, we have created a wishme() function that gives the functionality of greeting according to the system time to our A.I.
2. After wishme() function, we have created a takeCommand() function, which helps our A.I to take command from the user. This function is also responsible for returning the user's query in a string format.
3. We developed the code logic for opening different websites like google, youtube, and stack overflow.
4. At last, we added functionality to send emails.

# The E.N.D.
With this, you have successfully made your very first virtual assistant.
But, if we look at the very basic level, the sole purpose of A.I is to develop machines that can perform human tasks with the same effectiveness or even more effectively than humans.
