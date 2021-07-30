import random

import speech_recognition as sr #convert speech to text
import datetime #for fetching date and time
import playsound # to play saved mp3 file
from gtts import gTTS # google text to speech
import os # to save/open files
import wolframalpha # to calculate strings into formula
from selenium import webdriver # to control browser operations


jokes = ["What is fast, loud and crunchy? A rocket chip!",
         "How does a train eat? ",
         "Why can't you hear a Pterodactyl going to the bathroom? Because the P is silent.",
         "Whats blue and smells like red paint? Blue paint."
         ]

def talk():
    input = sr.Recognizer()
    with sr.Microphone() as source:
        audio = input.listen(source)
        data = ""
        try:
            data = input.recognize_google(audio)
            print("Your question is, " + data)

        except sr.UnknownValueError:
            print("Sorry I did not hear your question, Please repeat again.")


    return data

def respond(output):
    num=0
    print(output)
    num += 1
    response=gTTS(text=output, lang='en')
    file = str(num)+".mp3"
    response.save(file)
    playsound.playsound(file, True)
    os.remove(file)


if __name__ == '__main__':
    respond("Hi, I am Chatbot your personal assistant")

    while (1):
        respond("How can I help you?")
        text = talk().lower()

        if text == 0:
            continue

        if "stop" in str(text) or "exit" in str(text) or "bye" in str(text):
            respond("Ok bye and take care")
            break

        elif 'joke' in text:
            random_joke = random.choice(jokes)
            respond(random_joke)

        elif 'time' in text:
            strTime = datetime.datetime.now().strftime("%H:%M")
            respond(f"the time is {strTime}")

        elif 'date' in text:
            strDate = datetime.datetime.now().strftime("%d %b")
            respond(f"the date is {strDate}")

        elif "calculate" or "what is" in text:
            question = talk()
            app_id = "678E4V-X9U4UUVR85"
            client = wolframalpha.Client(app_id)
            res = client.query(text)
            answer = next(res.results).text
            respond("The answer is " + answer)

        else:
            respond("I'm not sure what to do")

