import speech_recognition as sr
from gtts import gTTS
import pygame
import time

### This is a helper class that provides both text-to-speech and speech-to-texts methods. ###
class Helper:

    
    language = 'en'
    listener = sr.Recognizer()
    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.5)
    
    def __init__(self, name = 'Alexa', path = 'audofile_path'):
        self.name = name
        self.lower_name = self.name.lower()
        self.audio_path = path

   # Converts input auto from the microphone to text, and returns that text as a string.
   # Outputs in the terminal what it hears from the mic if feedback is set to True. 
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
        
        while pygame.mixer.music.get_busy() == True:
            time.sleep(0.1)
            continue # keeping looping here so that the next audio doesn't overwite the audiofile playing


        speech = gTTS(text, lang = self.language, slow = False)
        speech.save(self.audio_path)
        pygame.mixer.music.load(self.audio_path)
        pygame.mixer.music.play()

    # Method to give a quick friendly audio message and say the name of the helper object.
    def say_hello(self):
        self.say_this('Hello! My name is ' + self.name + '. How can I help you?')