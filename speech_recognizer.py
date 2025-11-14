import speech_recognition as sr
from speech_recognition import WaitTimeoutError


def listen():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("Listening...")
        audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)

        try:
            text = recognizer.recognize_google(audio)
            print("You Said : " + text)
            return text
        except sr.UnknownValueError:
            return "Sorry, I could not understand."
        except sr.RequestError:
            return "Sorry, there was a connection issue."
        except WaitTimeoutError :
            return "Sorry, Error Occured"

if __name__ == "__main__" :
    a = listen()
    print(a)