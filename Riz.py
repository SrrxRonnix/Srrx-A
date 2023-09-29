import datetime
import pyttsx3
import requests
import speech_recognition
import speech_recognition as sr
import wikipedia


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty ("voices", voices[0].id)
rate = engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0.4)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"you said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"

    return query



if __name__ == "__main__":
    while True:
        qurery = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok Ronnix, Call me when you need me")
                    break

elif "hello" in query:
    speak("Hey Ronnix, Whats up ?")
elif "I am fine" in query:
    speak("That's Great, say what are you upto")




elif "google" in query:
    from SearchNow import searchGoogle
    searchGoogle(query)
elif "youtube" in query:
    from SearchNow import searchYoutube
    searchYoutube(query)
elif "wikipedia" in query:
    from SearchNow import searchWikipedia
    searchWikipedia(query)



elif "temparature" in query:
    search = "temparature in Kolkata"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifuSoup(r.text,"html.parser")
    temp = data.find('div', class_ = "BNeawe").text
    speak(f"current{search} is {temp}")

elif "weather" in query:
    search = "weather in Kolkata"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifuSoup(r.text,"html.parser")
    temp = data.find('div', class_ = "BNeawe").text
    speak(f"current{search} is {weather}")

elif "the time" in query:
    strTime = datetime.datetime.now().strftime("%H:%M")
    speak(f"Ronnix, the time is {strTime}")

elif "finally sleep" in query:
    speak("Going for a nap, Ronnix")
    exit()

