# PyHelper class demo
from PyHelper import Helper

# The default name of the helper class is 'Frank', but it can be set to any name.
alexa = Helper(name = 'Alexa')

# Give a quick audio greeting.
alexa.say_hello()

# Listen for a command from the microphone, and return what is heard as a string.
command = alexa.listen_for_command(feedback = True)

# Say as audio what command was heard. 
alexa.say_this('I heard you say: ' + command, feedback = True)

#alexa.print_voices()