# import speech_recognition as sr
import pyttsx3 as tts
import speech_recognition as sr

### This is a helper class that provides both text-to-speech and speech-to-texts methods. ###
class Helper:

    listener = sr.Recognizer()
    engine = tts.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    
    def __init__(self, name = 'Alexa'):
        self.name = name
        self.lower_name = self.name.lower()

#    Converts input audio from the microphone to text, and returns that text as a string.
#    Outputs in the terminal what it hears from the mic if feedback is set to True. 
    def listen_for_command(self, feedback = False):
        try:
            with sr.Microphone() as source:
                print(self.name + ': Listening...')
                voice = self.listener.listen(source)
                command = self.listener.recognize_google(voice)
                command = command.lower()

                hi_name = 'hi ' + self.lower_name + ' '
                name = self.lower_name + ' '

                if hi_name in command:
                    command = command.replace(hi_name, '')
                elif name  in command:
                    command = command.replace(name, '')

                if feedback == True:
                    print(self.name + ': Heard this as a command: ' + '"' + command + '."')

        except Exception as e:
            print(e)
            self.say_this("Sorry, I didn't quite get that. Could you try again later?")
        return command
    
   # Plays text input as audio, and outputs in the terminal what its trying to say if feedback is set to True.
    def say_this(self, text, feedback = False):

        if feedback == True:
            print(self.name + ': saying: ' + '"' + text + '."')

        self.engine.say(text)
        self.engine.runAndWait()

    # Method to give a quick friendly audio message and say the name of the helper object.
    def say_hello(self):
        self.say_this('Hello! My name is ' + self.name + '. How can I help you?')

    # Method to print the available voices to the terminal.
    def print_voices(self) :
        for voice in self.voices:
            # to get the info about various voices in our PC 
            print("Voice:")
            print("ID: %s" %voice.id)
            print("Name: %s" %voice.name)
            print("Age: %s" %voice.age)
            print("Gender: %s" %voice.gender)
            print("Languages Known: %s" %voice.languages)