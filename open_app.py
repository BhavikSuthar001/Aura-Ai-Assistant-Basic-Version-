import pyautogui
import time
from speech_recognizer import listen
from speak import speak


def OpenApp():
    speak("What App do you want to open?")
    software = listen() #open {software}

    app = software.split(" ")

    # OpenAI(software)
    speak(f"Your App is Opening")
    pyautogui.click(630 , 1049)
    time.sleep(0.5)
    pyautogui.write(f"{app[-1]}", interval=0.5)
    time.sleep(0.5)
    pyautogui.leftClick(681 , 264)
    time.sleep(0.5)


if __name__ == "__main__":
    OpenApp()