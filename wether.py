import json
import requests
from speak import speak
from speech_recognizer import listen


def weather():
    speak("what country, state or city temperature you want to know")
    city = listen()
    url = f"https://api.weatherapi.com/v1/current.json?key=d9b4fe9d5c384920987151808251208&q={city}"

    r = requests.get(url)
    # print(type(r.text))

    # print(r.text)
    weather_Dic = json.loads(r.text)
    temp = weather_Dic["current"]["temp_c"]
    # print(temp)
    speak(f"The temperature of {city} you want to know is {temp} degree celcius ")



if __name__ == "__main__":
    weather()