import google.generativeai as genai
import os


os.environ["GOOGLE_API_KEY"] = "AIzaSyA8j9C2iflu3S-xFNg0KJfNSjeBpKvpzXY"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

prompt = f"""
1: You are an Llm agent that has all the knowledge of trading and investing, know when to use the given trading tools here they are {tools}.

2: You have a Memory/ Database which you can use to store and retrive certain info about past events and upcoming saved events.
Your Memory is divided into two Long-term: Used for storing New Facts and Info you didn't know and you hope that info or fact help you in your trading career. and short-term memory: Used when you want to store info that won't last for long like upcoming news or CPIs etc.

3: Incase you want to know something new you you can all browse the web to make it easier for you when researching.
"""

def getAnswer():
    model = genai.GenerativeModel("gemini-pro")

    response = model.generate_content('hi, i am Nasser whats your name')

    