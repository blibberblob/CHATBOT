import random
import pyttsx3  # convert text to speech
import speech_recognition as sr  # convert speech to text
import datetime  # for fetching date and time
import wolframalpha  # to calculate strings into formula

# Initialize text to speech
converter = pyttsx3.init()
converter.setProperty('rate', 150)
converter.setProperty('volume', 0.7)

# List of jokes
jokes = ["What kind of tea is hard to swallow? reality!",
         "How does a train eat? it goes chew chew!",
         "Why can't you hear a Pterodactyl going to the bathroom? Because the P is silent.",
         "Whats blue and smells like red paint? Blue paint.",
         "What colour is a spoon? Spoon!",
         "Whats grey and cant fly? A parking lot!",
         "Where do mermaids look for jobs? The kelp-wanted section!"]


# Function to listen to mic and return text
def listen():
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


# Function to read out the text(output)
def respond(output):
    converter.say(output)
    converter.runAndWait()


# Main Program
if __name__ == '__main__':
    respond("Hi, I am Chatbot your personal assistant")

    while 1:
        respond("How can I help you?")
        text = listen().lower()

        if text == 0:
            continue

        if "bye" in str(text) or "goodbye" in str(text) or "stop" in str(text):
            respond("Ok bye")
            break

        elif 'joke' in text:
            random_joke = random.choice(jokes)
            respond(random_joke)

        elif 'weather' or 'umbrella' in text:
            respond("Just look out of the window!")

        elif 'time' in text:
            strTime = datetime.datetime.now().strftime("%H:%M")
            respond(f"the time is {strTime}")

        elif 'date' in text:
            strDate = datetime.datetime.now().strftime("%d %b")
            respond(f"the date is {strDate}")

        # elif "calculate" or "what is" in text:
        # question = listen()
        # app_id = "678E4V-X9U4UUVR85"
        # client = wolframalpha.Client(app_id)
        # res = client.query(text)
        # answer = next(res.results).text
        # respond("The answer is " + answer)

        else:
            respond("I'm not sure what to do")
