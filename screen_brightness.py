import screen_brightness_control as sbc
import re
from speech_recognizer import listen
from speak import speak

def set_screen_brightness():
    speak("How much brightness do you want?")
    task = listen()
    num = re.findall(r'\d+', task)
    if num:
        brightness = int(num[0])
        sbc.set_brightness(brightness)
        speak(f"Brightness set to {brightness} percentage")
    else:
        print("Invalid input")



if __name__ == "__main__":
    set_screen_brightness()
