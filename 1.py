import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import sys
from selenium import webdriver
import pywhatkit

r = sr.Recognizer()
m = sr.Microphone()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()


def searchyoutube():
    speak('content:')
    # query = str(input('command: '))
    query = myCommand()
    print(f'You said {query}')
    # query = query.lower()
    browser = webdriver.Chrome()
    browser.get('https://youtube.com')
    search = browser.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
    search.send_keys(query)
    searchbutton = browser.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button')
    searchbutton.click()


def myCommand():
    global query
    try:
        query = str(input('command: '))
        query = query.lower()
    except Exception as ex:
        speak(ex)
    return query


def greetMe():
    present = int(datetime.datetime.now().hour)
    if 0 <= present < 12:
        speak('Good Morning!')
    elif 12 <= present < 18:
        speak('Good Afternoon!')
    elif present >= 18 and present != 0:
        speak('Good Evening!')

def whatsapp():
    try:
        print('please enter mobile number')
        no = input()
        print('enter the message')
        msg = input()
        print('enter the time to send')
        h,m = map(int,input().split())
        pywhatkit.sendwhatmsg("+91"+no,msg,h, m,wait_time=10)
        print("Sent")
    except:
        print('unexpected error occured')


try:
    greetMe()
    speak('Hello , I am jarvis')
    speak('How may I help you?')
    while True:
        with m as source:
            audio = r.listen(source)
        try:
            value = r.recognize_google(audio).lower()
            speak('got it!')
            print(f"You said {value}")
            if value == 'exit' or value == 'quit' in value:
                sys.exit()
            elif value == 'open google' or value == 'google':
                webbrowser.open('www.google.com')
            elif value == 'search youtube':
                searchyoutube()
            elif value == 'open yahoo' or value == 'yahoo':
                webbrowser.open('www.yahoo.com')
            elif value == 'whatsapp':
                whatsapp()
        except sr.UnknownValueError:
            speak("didn't hear say again!!")
except KeyboardInterrupt:
    pass
