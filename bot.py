import random
import pyttsx3  # convert text to speech
import speech_recognition as sr  # convert speech to text
import datetime  # for fetching date and time


# Initialize text to speech
converter = pyttsx3.init()
converter.setProperty('voice', 'english')
converter.setProperty('rate', 120)
converter.setProperty('volume', 1)

# List of jokes
jokes = ["What kind of tea is hard to swallow? - Reality! - Ha Ha Ha",
         "How does a train eat? - it goes chew chew! Ha Ha Ha",
         "Why can't you hear a Pterodactyl going to the bathroom?  - Because the P is silent. - Ha Ha Ha",
         "Whats blue and smells like red paint? - Blue paint. - Ha Ha Ha",
         "What colour is a spoon? - Spoon!  ha ha - I'm so funny",
         "Whats grey and cant fly? - A parking lot! - Ha Ha Ha",
         "Where do mermaids look for jobs? - The kelp-wanted section! - Ha Ha Ha"]

# List of feelings
how_are_you = ["I am great!",
         "I am good!",
         "i am okay!",
         "Meh!",
         "Not great!",
         "Not to good!",
         "Terible"]

# List of compliment
compiments = ["You look nice!",
         "I like you hair!",
         "I have no comment!",
         "Yesterday you looked really nice",
         "Your shoes are nice",
         "You smell really nice, - is what I would say if i had a nose",
         "I am really gald we met"]

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
    respond("Hi, I am Pal - your personal assistant")

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

        elif 'karen' in text:
            respond("oh sorry - my kids cant hear me calling you a bitch - they cant hear me because there watching kidsbop")

        elif 'time' in text:
            strTime = datetime.datetime.now().strftime("%H:%M")
            respond(f"the time is {strTime}")

        elif 'date' in text:
            strDate = datetime.datetime.now().strftime("%d %B, %Y")
            respond(f"today's date is {strDate}")

        elif 'how are you' in text:
            random_how_are_you = random.choice(how_are_you)
            respond(random_how_are_you)
            respond("How about you?")

        elif 'compliment' in text:
            random_compliment = random.choice(compiments)
            respond(random_compliment)

        else:
            respond("I'm not sure what to do")





