import time
import pygame
import sys
from speech_recognizer import listen
from speak import speak
from web_module import open_youtube, open_x, open_gmail, open_github , open_google, open_instagram, open_facebook, open_linkedin
from wether import weather
from battery_percentage import battery_percentage
from colorama import Fore ,init
from open_app import OpenApp
from screen_brightness import set_screen_brightness

init()

#For alarm Clock
def alarm() :
    pygame.mixer.init()
    pygame.mixer.music.load(r"E:\\MegaProject\\iphone_alarm.mp3")
    pygame.mixer.music.play(loops=-1)

#For Time and Greating
def time_greating() :
    timestamp = time.strftime("%H:%M:%S")
    # Get the current time

    print("Current Time:", timestamp)

    if "05:00:00" <= timestamp < "12:00:00":
        speak("Good morning sir")
        print("Good Morning Sir")
    elif "12:00:00" <= timestamp < "17:00:00":
        speak("Good Afternoon Sir")
        print("Good Afternoon Sir")
    elif "17:00:00" <= timestamp < "21:00:00":
        speak("Good Evening Sir")
        print("Good Evening Sir")
    else:
        speak("Good Night Sir")
        print("Good Night Sir")

#For Animation
def anim(text, delay=0.07):

    for char in text :
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

#Main Command Processing Function
def processcommand():
    while True:
        command = listen()
        TASKS = {
            "open youtube" : open_youtube,
            "open x" : open_x,
            "open gmail" : open_gmail,
            "open github" : open_github,
            "open google" : open_google,
            "open instagram" : open_instagram,
            "open facebook" : open_facebook,
            "open linkedin" : open_linkedin,
            "weather" : lambda : weather(),
            "battery" : lambda : battery_percentage(),
            "set brightness" : lambda : set_screen_brightness(),
            "open app": lambda : OpenApp()
        }
        # check if command matches any task
        found = False
        for key, action in TASKS.items():
            if key in command.lower():
                action() # run the matched function
                # gemini(command)
                found = True
                break

        if not found:
            print("Task not found")

if __name__ == "__main__":
    speak("assistant is ready")
    while True:
        command = listen().lower()
        if "hello" in command:
            anim(Fore.CYAN + "Initializing Aura....")
            time.sleep(0.05)
            anim(Fore.GREEN + "Activating all Systems....")
            time.sleep(0.05)
            anim(Fore.GREEN + "Initializing all features....")
            time.sleep(0.05)
            anim(Fore.MAGENTA + "Aura Initialised Succesfully....")
            time.sleep(0.05)
            anim(Fore.MAGENTA + "Hello Sir, How can i helped you?")
            speak("Hello Sir, How can i helped you?")
            time.sleep(0.05)
            print("Aura is Listening...")
            time_great = time_greating
            gemini(time_great)
            processcommand()
        elif command == "shutdown" or command == "shut down":
            speak("Aura Succesfully Shutting Down....")
            break


        
