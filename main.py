import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    '''
    DOC STRING

    '''
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning PD")
    elif hour>=12 and hour<17:
        speak("Good Afternoon PD")
    elif hour>=17 and hour<23:
        speak("Good Evening PD")
    else:
        speak("Good Night PD, Be More Productive Tomorrow??")

    speak("I am Jarvis Your Customized AI, How May I help You?")

def takeCommand():
    '''
        It takes input from microphone from the user and returns string output

    '''
    r = sr.Recognizer()
    with sr.Recognizer as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said : {query}\n")
    
    except Exception as e:
        print(e)

        print("Say that again please...")
        return "None"

if __name__=="__main__" :
    wishMe()    
    takeCommand()
