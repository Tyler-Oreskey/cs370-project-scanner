_______________________________________________________________________________________________________________
Description:

PyHelper2 is a module that provides both text-to-speech and speech-to-texts methods through the Helper class.
To install the libraries needed to run the program, execute the commands below in the terminal:

_______________________________________________________________________________________________________________
Installation:
# For the speech-to-text libraries:
    pip install SpeechRecognition

# For the text-to-speech libraries:
    pip install gTTS

# For python-vlc libraries:
    pip install python-vlc

  
## Pyaudio is also needed to use the speech recognition with a microphone.

to install the needed libraries:
    sudo apt-get install portaudio19-dev python-all-dev python3-all-dev && sudo pip3 install pyaudio

_______________________________________________________________________________________________________________
Import:

to import the helper class:

    from PyHelper2 import Helper
    import mute_alsa

_______________________________________________________________________________________________________________
Methods:

    1. instance_name = Helper(name = 'chosen_name', path = 'mp3_audio_file_path')

    - This is the constructor method to instantiate an instance of the Helper class. As arguments, it takes
      an optional name argument as a string, and the path to a blank .mp3 or .wav file also as a string.
      If no name is given, the default name is "Alexa". The supplied audio file with be overwritten for 
      the text-to-speech functionality of the class.

    
    2. say_this('message', feedback = False)

    - Text-to-speech method that outputs the google tts version of a string when supplied as an argument. If 
      feedback is set to "True", it will also output to the terminal what class is attempting to say.


    3. listen_for_command(feedback = False)

    - Speech-to-text method that listens for audio from a default microphone and returns as a string the command
      it hears, without the given name of the class if it was spoken. If feedback is set to "True" it will print to 
      the terminal the command it heard from audio input.


    4. say_hello()

    - Outputs a quick hello message as audio, saying "hello, My name is <name>". The name
      will be the one chosen when the class was instantiated.

_______________________________________________________________________________________________________________
Examples:

To get a quick feel for how the program might work, run the PyHelper_demo.py file in VSCode
and try answering 'yes', 'no', or something else when asked if you want to scan something. (The default name
is Alexa, but it can be changed to whatever we would like it to be for the project)

_______________________________________________________________________________________________________________
More:

For more information for the dependencies of this class, see the links below:

1. SpeechRecognition:
https://pypi.org/project/SpeechRecognition/

2. Google text-to-speech:
https://pypi.org/project/gTTS/

3. Python-VLC:
https://pypi.org/project/python-vlc/

4. Pyaudio: 
https://pypi.org/project/PyAudio/