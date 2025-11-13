import psutil
from speak import speak
import time
from speech_recognizer import listen

def battery_percentage():
    battery = psutil.sensors_battery()
    speak(f"The Battery percentage is {battery[0]} Percentage.")

def notify_battery(nft):
    speak("at what batter percentage you want to notify to remove laptop from charging? ")
    nft = listen()
    while True:
        battery = psutil.sensors_battery()
        if battery[0] == int(nft):
            speak(f"Sir Battery Percentage is now {battery[0]} Percentage Please Remove laptop from charger.")
            break
        time.sleep(10)


