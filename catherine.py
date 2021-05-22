from gtts import gTTS
import playsound
from datetime import datetime
now = datetime.now()  # current date and time

# function that speaks with gTTS


def speak(text):
    # function that speaks out using gTTS
    tts = gTTS(text=text, lang="en")
    fileName = "voice.mp3"
    tts.save(fileName)
    playsound.playsound(fileName)


def time():
    # function that says the time
    time = now.strftime("%H:%M%p")
    speak("The current time is "+time)


def date():
    # function that says the date
    date = now.strftime("%d %B, %Y")
    speak("Today's date is "+date)


time()
date()
speak("Hi Fotie, How may i help you? ")
