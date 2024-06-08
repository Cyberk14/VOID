import google.generativeai as genai
import os


os.environ["GOOGLE_API_KEY"] = "AIzaSyA8j9C2iflu3S-xFNg0KJfNSjeBpKvpzXY"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
