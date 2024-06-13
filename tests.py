import google.generativeai as genai # type: ignore
import os
import PIL.Image
from Head.Control.Brain.brain import init_message

os.environ["API_KEY"] = "AIzaSyA8j9C2iflu3S-xFNg0KJfNSjeBpKvpzXY"

genai.configure(api_key=os.environ['API_KEY'])

model = genai.GenerativeModel(model_name='models/gemini-1.5-flash-latest')

def send(arg: str, image=None):
    if image is None:
        arg = f"""
        ||| {init_message} |||
        
        ||| {arg} |||
        """
        response = model.generate_content(arg) # type: ignore
        return response.text

    elif arg and image is True:
        image = PIL.Image.open(image)
        response = model.generate_content([arg, image])
        return response.text

# The `while True` loop in the code snippet is creating an infinite loop that continuously prompts the
# user for input using the `input("prompt: ")` function.
while True:
    Inp = input("prompt: ")

    res = send(Inp)
    print(f"response: {res}")
