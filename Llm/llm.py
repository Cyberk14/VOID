import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

class Model:
    def __init__(self, text, **kwargs):
        for key, values in kwargs:
            if key == model:
                self.model = model
        self.text = text
        return self.model, self.text

    def GoogleModel(self, modelName="gemini-1.0-pro", self.text):
        model = genai.GenerativeModels(modelName)

        response 




