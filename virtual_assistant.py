import speech_recognition as sr
import playsound
from gtts import gTTS
import random
from time import ctime, time
import webbrowser
import os
import pyttsx3
import subprocess
import datetime

class Person:
    name = ''

    def setName(self, name):
        self.name = name


class MyVA:
    name = ''

    def setName(self, name):
        self.name = name


def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True


def engine_speak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en')
    rand_num = random.randint(1, 2000000)
    audio_file = 'audio' + str(rand_num) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(asis_obj.name + ":" + audio_string)
    os.remove(audio_file)


r = sr.Recognizer()


# get the string and audio file
def record_audio(ask=""):
    with sr.Microphone() as source:
        if ask:
            engine_speak(ask)
        audio = r.listen(source, 5, 5)
        print("looking at the database")
        voiceData = ''
        try:
            voiceData = r.recognize_google(audio)
        except sr.UnknownValueError:
            engine_speak('Sorry. Could not understand you')

        except sr.RequestError:
            engine_speak('Sorry , my server is down.')

        print(">>", voiceData.lower())
        return voiceData.lower()


def respond(voiceData):
    # greeting
    if there_exists(['hay', 'hi', 'hey', 'hai', 'hallo', 'hello', 'hola,', 'whatsup']):
        greetings = ["hi,what are we going to do" + person_obj.name, "Hi ,how can I help you" + person_obj.name,
                     "whatsup" + person_obj.name]

        greet = greetings[random.randint(0, len(greetings) - 1)]
        engine_speak(greet)

    if there_exists(["what is your name", "what's your name", "Tell me your name"]):
        if person_obj.name:
            engine_speak("my name is wanda")
        else:
            engine_speak("my name is Wanda. What's your name?")

    # asking name
    if there_exists(["my name is", "I am"]):
        person_name = voiceData.split("is")[-1].strip()
        engine_speak(f"okay, I will remember your name {person_name}")
        person_obj.setName(person_name)  # remember name in person object

    # google browsing
    if there_exists(["search for"]) and 'youtube' not in voiceData:
        search_term = voiceData.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is What I found for " + search_term + "on google")

    # youtube browsing
    if there_exists(["search youtube for"]):
        search_term = voiceData.split("for")[-1]
        url2 = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url2)
        engine_speak("here is what I found for " + search_term + "on youtube")

    # terminate program
    if there_exists(["exit", "tata", "bye", "bye bye", "quit", "goodbye"]):
        engine_speak("Goodbye! See You!")
        exit()

    # current time
    if there_exists(["what is the time", "tell me the time", "what time is it"]):
        current_time = ctime().split(" ")[3].split(":")[0:2]
        if current_time[0] == "00":
            hours = '12'
        else:
            hours = current_time[0]
        minutes = current_time[1]
        current_time = f'{hours} {minutes}'
        engine_speak(current_time)

    # quick games
    if there_exists(["open a quick game"]):
        url3 = "https://quickdraw.withgoogle.com/"
        webbrowser.get().open(url3)
        engine_speak("Opening Quick Draw game from the web!")

    # word
    if there_exists(["open word"]):
        engine_speak("Opening Microsoft Word")
        os.startfile(
            "C:\\Program Files\\Microsoft Office\\root\Office16\\WINWORD.EXE")

    # Open facebook
    if there_exists(["go to facebook"]):
        url = "https://www.facebook.com/"
        webbrowser.get().open(url)
        engine_speak("Welcome to facebook home page")

    # Print file source in console
    if there_exists(["show source"]):
        fh = open("D:\hai.txt")
        print(fh.readline())
        engine_speak("your file and file have ")

    # Open any folder in specific drives
    if there_exists(["open folder"]):
        search_term = "G:\\" + voiceData.split("folder ")[-1]
        webbrowser.open('file://' + search_term)
        engine_speak("opening that folder")

    # Launch application
    if there_exists(["open now"]):
        search_term = voiceData.split("now ")[-1]
        if search_term == 'notepad':
            search_term = 'C:\\Program Files\\Notepad++\\notepad++.exe'
        if search_term == 'spotify':
            search_term = 'C:\\Users\\Huzaifa\\AppData\\Roaming\\Spotify\\spotify.exe'
        print(search_term)
        subprocess.Popen(search_term)
        engine_speak("Welcome to see you back on " +
                     voiceData.split("now ")[-1])

    # Wait some time
    if there_exists(["wait"]):
        print("Wait once a minute.")
        engine_speak("I will wait for a minute")
        time.sleep(60)

    # loveCaculater
    if there_exists(["loves"]):
        def calculate(t):
            size = t.__len__()
            ttt = []
            for i in range(int(size/2)):
                tt = t[i]+t[size-i-1]
                ttt.append(tt)
            size = ttt.__len__()
            return ttt, size
        names = voiceData.split(" loves ")
        name1 = names[0]
        name2 = names[1]
        count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        name1 = name1.lower()
        name2 = name2.lower()
        for c in name1:
            count[ord(c)-96] += 1
        for c in name2:
            count[ord(c)-96] += 1
        t = []
        for c in count:
            if c != 0:
                t.append(c)

        while True:
            t, size = calculate(t)
            if size == 2:
                percentage = str(t[0]*10+t[1])
                engine_speak(name1+" loves "+name2+" "+percentage+"%")
                break

    # Weather check
    if there_exists(["What is today's weather", "Tell me today's weather","weather"]):
        voice_datacity=""
        voice_datacountry=""
        while True:
            voice_datacountry = record_audio("Tell me the name of the country you are in")
            if voice_datacountry.__len__()>1:
                break
        while True:
            voice_datacity = record_audio("Tell me the name of the city you are in")
            if voice_datacity.__len__()>1:
                break
        url4 = "https://www.google.com/search?q=weather+in+"+voice_datacountry+"+"+voice_datacity
        webbrowser.get().open(url4)
        engine_speak("Today's weather in ")

    # current location as per google Maps
    if there_exists(["what is my exact location"]):
        url = "https://www.google.com/maps/search/where+am+I+?/"
        webbrowser.get().open(url)
        engine_speak("You must be somewhere near here, as per google maps ")


person_obj = Person()
asis_obj = MyVA()
asis_obj.name = 'Wanda'
engine = pyttsx3.init()

hour = datetime.datetime.now().hour
if hour >= 6 and hour < 12:
    voice_data= record_audio("Hello,Good Morning")
    print("Hello,Good Morning")
elif hour >= 12 and hour < 18:
    voice_data= record_audio("Hello,Good Afternoon")
    print("Hello,Good Afternoon")
else:
    voice_data= record_audio("Hello,Good Evening")
    print("Hello,Good Evening")
print("You Said :", voice_data)
respond(voice_data)

while True:
    voice_data = record_audio("Anything you wanna say?")
    print("You said:", voice_data)

    respond(voice_data)
