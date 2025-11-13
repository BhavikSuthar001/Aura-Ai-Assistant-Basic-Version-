import pyttsx3

def speak(command):
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.say(command)
    engine.runAndWait()