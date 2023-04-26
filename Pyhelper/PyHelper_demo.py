# This is the updated Helper class demo from the PyHelper2 module.
from PyHelper2 import Helper
import mute_alsa

# The default name of the helper class is 'Alexa', but it can be set to any name.
alex = Helper(name = 'alex', path = '/home/tpores/Desktop/say_this.mp3')

# Give a quick audio greeting.
alex.say_hello()

# Ask the user if they want to scan somthing.
alex.say_this("Do you want me to scan something for you?", feedback = True)

# Listen for a command from the microphone and return what is heard as a string if feedback is set to True.
command = alex.listen_for_command(feedback = True)
if alex.done_listening == True:
    for i in range(3):
        if alex.done_listening == True:
            if 'yes' in command:
                alex.say_this(" Ok, go ahead and scan the code when you're ready", feedback = True)
                break
            elif 'no' in command:
                alex.say_this("Alright! hope you have a good day!", feedback = True)
                break
            elif i < 2:
                alex.say_this(" hmm, I didn't quite get that. Could you say it again?", feedback = True)
                command = alex.listen_for_command(feedback = True)
            else:
                alex.say_this("hmm sorry, for some reason I seem to be having a hard time understanding you right now. Try again later.", feedback = True)
                break
    