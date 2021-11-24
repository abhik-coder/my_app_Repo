import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening to your command...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
                return(command)
                
    except:
        pass
    


def power_on():
    def run_alexa():
        command = take_command()
        if 'play video' in command:
            song = command.replace('play video', '')
            talk('Playing' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            talk('The time is' + time)
        elif 'wikipedia' in command:
            name = command.replace('wikipedia', '')
            info = wikipedia.summary(name, 1)
            print(info)
            talk(info)
        elif 'hello' in command:
            talk('Hello, my name is Alexa')
        elif 'how are you' in command:
            talk('I am doing great')
        elif 'play game' in command:
            game = command.replace('play game', '')
            talk('Ok I will search ' + game + ' game on Google')
            pywhatkit.search(game + ' online game')
        if 'i am angry' in command:
            talk('Please do something to cheer you up. You can cheer up by putting happy music, do meditation, etc')
            pywhatkit.playonyt('meditation')
        elif 'i am sad' in command:
            talk('Please do something to cheer you up like you can tell me to put a joke')
        elif 'i am happy' in command:
            talk('Oh, that is great! What can I do for you?')
        elif 'tell me a joke' in command:
            talk(pyjokes.get_joke())
        elif 'are you there' in command:
            talk('Yes, I am there. What can I do for you?')
        if 'reload' in command:
            talk('RELOADING PLEASE WAIT FOR A WHILE...')
            power_on()
        else:
            talk('Umm I could not understand. Can you please repeat it again')


    while True:
        command = take_command()
        if  'bye' in command:
            talk("Goodbye!")
            break
        else:  
            run_alexa()  
            
            

power_on()