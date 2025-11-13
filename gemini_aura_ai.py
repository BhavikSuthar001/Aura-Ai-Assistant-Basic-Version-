import google.generativeai as genai
from speak import speak

def gemini(command):
    api_key = ""
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"you are my personal assistant whose name is AURA dont forget and i your sir Bhavik Suthar. make sure when i give you any task or command than give that ans in 2 - 3 sentence in simple form not in long also talk with me like an freind. i am an btech in Ai and data science student. be my assistant who always talk with me like jarvis from iron man movie. talk me in only english language and be nice to me. Also you dont have to say my surname only bhavik and dont talk about my degree just follow my work which i am going to give you and also you dont have to say about you that you are aura only say the answer of my question : {command}"
    response = model.generate_content(prompt)
    speak(response.text)