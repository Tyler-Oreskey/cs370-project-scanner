import speech_recognition as sr
from gtts import gTTS
import vlc
import time
import mute_alsa # mudule needed to mute unneeded alsa warnings.

### This is a helper class that provides both text-to-speech and speech-to-texts methods. ###
class Helper:
    
    language = 'en'
    listener = sr.Recognizer()
    media_player = vlc.MediaPlayer()
    done_listening = True    # a public data member to see if the class is currently playing an audio clip. can be used to control whether or not a clip should play while alexa is also listening.

    def __init__(self, name = 'Alexa', path = 'audofile_path'):
        self.name = name
        self.lower_name = self.name.lower()
        self.audio_path = path
        self.media = vlc.Media(path)
    
   # Converts input auto from the microphone to text, and returns that text as a string.
   # Outputs in the terminal what it hears from the mic if feedback is set to True.
    def listen_for_command(self, feedback = False):

        command = '_err_empty_comand_'
        self.done_listening = False

        try:
            with sr.Microphone() as source:
                print(self.name + ': Listening...')
                audio = self.listener.adjust_for_ambient_noise(source)
                audio = self.listener.listen(source)
                command = self.listener.recognize_google(audio)
                command = command.lower()

                hi_name = 'hi ' + self.lower_name + ' '
                name = self.lower_name + ' '

                if hi_name in command:
                    command = command.replace(hi_name, '')
                elif name  in command:
                    command = command.replace(name, '')

                if feedback == True:
                    print(self.name + ': Heard this as a command: ' + '"' + command + '."')

        except sr.UnknownValueError:
            print("The speech recognition engine was not able to understand this audio")
        except sr.RequestError as e:
            print("Request from Google speech recognition service failed; {0}".format(e))
        finally:
            self.done_listening = True
        return command
    
   # Plays text input as audio, and outputs in the terminal what its trying to say if feedback is set to True.
    def say_this(self, text, feedback = False):

        time.sleep(0.1) # sleep here so that the class has time to start playing before we check it's status in the while loop below.

        #while self.media_player.is_playing() == 1 or self.done_listening != True:
        while self.media_player.is_playing() == 1:
            time.sleep(0.01) # check to see if a clip is already playing, and sleep for a short amount of time if so.

        if feedback == True:
            print(self.name + ': saying: ' + '"' + text + '."')
        
        speech = gTTS(text, lang = self.language, slow = False)
        speech.save(self.audio_path)

        self.media = vlc.Media(self.audio_path)
        self.media_player.set_media(self.media)
        self.media_player.play()
        time.sleep(0.1) # sleep here again to give the class time to play the clip.

    # Method to give a quick friendly audio message and say the name of the helper object.
    def say_hello(self):
        self.say_this('hmm Hello! My name is ' + self.name)