import random
import pyttsx3  # convert text to speech
import speech_recognition as sr  # convert speech to text
import datetime  # for fetching date and time


# Initialize text to speech
converter = pyttsx3.init()
converter.setProperty('voice', 'english')
converter.setProperty('rate', 140)
converter.setProperty('volume', 0.7)

# List of jokes
jokes = ["What kind of tea is hard to swallow? - Reality!",
         "How does a train eat? - it goes chew chew!",
         "Why can't you hear a Pterodactyl going to the bathroom?  - Because the P is silent.",
         "Whats blue and smells like red paint? - Blue paint.",
         "What colour is a spoon? - Spoon!",
         "Whats grey and cant fly? - A parking lot!",
         "Where do mermaids look for jobs? - The kelp-wanted section!"]

# List of feelings
how_are_you = ["im great!",
         "im good!",
         "im okay!",
         "meh!",
         "not great!",
         "not to good!",
         "terible"]


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
    respond("Hi, I am P - A - L - your personal assistant")

    while 1:
        respond("How can I help you?")
        text = listen().lower()

        if text == 0:
            continue

        if "bye" in text or "goodbye" in text or "stop" in text:
            respond("Good bye")
            break

        elif 'joke' in text:
            random_joke = random.choice(jokes)
            respond(random_joke)

        elif 'weather' in text or 'rain' in text or 'umbrella' in text:
            respond("Just look out of the window!")

        elif 'Naz' in text:
            respond("give Naz a guinea pig, give Naz a guinea pig Come on, papa")

        elif 'time' in text:
            strTime = datetime.datetime.now().strftime("%H:%M")
            respond(f"the time is {strTime}")

        elif 'date' in text:
            strDate = datetime.datetime.now().strftime("%d %B, %Y")
            respond(f"today's date is {strDate}")

        elif 'how are you' in text:
            random_how_are_you = random.choice(how_are_you)
            respond(random_how_are_you)
            respond("how about you?")

        else:
            respond("I'm not sure what to do")





