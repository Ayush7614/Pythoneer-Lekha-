import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random

#====================================================================================
engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',170)
#====================================================================================

#======================MSG====================================================>>>>>>>>>>>>

greet={1:"Bonjour",2:"Hello,Let us begin our new day!",3:"Good Morning"}
welcome={1:"Not at all! Sir",2:"It's my duty Sir!",3:"Don't mention it!! Sir",4:"It's my pleasure to serve you, My Liege"}

#======================FUNCTIONS====================================================>>>>>>>>>>>>

def speak(audio):
    print("   ")
    print(f": {audio}")
    print("   ")
    engine.say(audio)
    engine.runAndWait()

def wishME():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        a=random.randint(1,4)
        speak(greet[a])
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am ready to serve you!!")

def takecommad():
    #take audio input and returns string

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:

        speak("Sorry Sir!! please say that again")
        return "None"
    return query

def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','password')      #pls replace it with your email ID and password to see the change
    server.sendmail('youremail@gmail.com',to,content)
    server.close()
    

#======================JARVIS-TALKS====================================================>>>>>>>>>>>>
if __name__ == "__main__":
    wishME()
    while True:
        query=takecommad().lower()         #taking task in query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace('wikipedia',"")
            results = wikipedia.summary(query,sentences=1)
            speak('Accordind to Wikipedia!!')
            print(results)
            speak(results)
        
        elif 'how are you' in query:
            speak("I am doing just fine!! and woking")

        elif 'open youtube' in query or 'on youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_que='E:\\music'
            songs=os.listdir(music_que)
            print(songs)
            os.startfile(os.path.join(music_que,songs[0]))

        elif 'the time' in query:
            startime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {startime}")
        
        elif 'open code' in query:
            vsc_path="C:\\Users\\Tanishq\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vsc_path)

        elif "email to me" in query:
            try:
                speak("What should I say?")
                content=takecommad()
                to="thecriminal480@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!!")
            except Exception as e:
                print(e)
                speak("Sorry Sir!! I am not able to send email this time...")
        
        elif "who are you" in query:
            speak("I  am  Jarvis!!, an AI program created by my Lord for making his life easier,Though he did not need me but one day i prove myself that i am worthy!! ")

        elif "go to hell" in query:
            speak("sorry sir! i know i am not the best ... but i trying to improve myself everyday ")
            exit()

        elif "take care" in query:
            speak("Bye sir! You can call me gain anytime")
            exit()

        elif "good" in query or "nice work" in query or "thank" in query:
            x=random.randint(1,5)
            speak(welcome[x])
            
         

