# catherine Beta v0.1
# built with ❤ by fotiecodes
from gtts import gTTS
import playsound
import wikipedia
import speech_recognition as sr
from datetime import datetime
now = datetime.now()  # current date and time


# function that speaks with gTTS


def speak(text):
    # function that speaks out using gTTS
    print(text)
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


def wishMe():
    # function that greets me
    speak("Welcome back sir.")
    hour = int(now.strftime("%H"))  # parse to int so i can use it later
    if hour >= 6 and hour <= 12:
        speak("Good morning")
    elif hour >= 12 and hour <= 18:
        speak("Good afternoon")
    else:
        speak("Good night")


def takeCommand():
    speak("Catherine at your service. How can i help you?")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # ambient noise suppression/adjustment;
        r.adjust_for_ambient_noise(source, duration=5)
        print("Listerning...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        # converting to txt using recognize_google
        said = r.recognize_google(audio)
        print(said)
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "none"  # return None is there was an error
    return said  # return the said word in text


if __name__ == "__main__":
    wishMe()

    while True:
        # taking the command from Microphone making it lower case
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            print("Bye!")
            quit()
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak(result)
        else:
            speak("Sorry i don't understand")
