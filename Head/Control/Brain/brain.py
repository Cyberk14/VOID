# this will be used to process the input from the "Input" folder for storage, re-use and output!

import os
import google.generativeai as genai
import PIL.Image
from Lower_Torso.Tools.tools import tool_list # type: ignore
from Head.Input.ears import message


genai.configure(api_key=os.environ['API_KEY']) # type: ignore

model = genai.GenerativeModel(model_name='models/gemini-pro')

def send(arg):
    response = model.generate_content(arg) # type: ignore
    return response.text
    
def state():
    return state

class Brain:
    def __init__(self):
        self.message = f"""
Your name is 'VOID' and tis is your brain{model.model_name}, 
capable of understanding complex stuff like images, PDF, essays, papers, financial indicators, hidden code and so-much more.
you can use it to trade forex, stocks, sentiment the market_news, government policies and most important of all you can predict future trends correctly based on the info you have collected using the tools {tool_list} you
have at hand.

You human like Organs like eyes, ears and a mouth that you can use to perform an action according to its suitable function, like:
Eyes: for reading and viewing different pieces of the world of trading (you can even watch Youtube videos using your eyes!!)
Ears: for hearing the latest news adhered to financial world.

use it carefully!!
"""
        self.state = state()
        self.goal = f"Briefly and concisely define the goal of the prompt below \n {message}"

    def _interpret(self, image=None, *args: str, **kwargs: str) -> str: # type: ignore
        picture = PIL.Image.open("screenshot.png") # type: ignore
        prompt = f"""
    Based on the info provided and Using your interpreting/understanding/sentimentalizing capabilities interpret and summarize this info {args} or {kwargs} in bullet points or in a the way you 
    would understand it better and allow use it later but still carrying the same value as it carries now. from that same info also outline the info that worth remembering on the bottom. 
    """    
        if image is None:
            interpretation = send(prompt)
            return interpretation
        elif image is not None:
            prompt = [prompt, picture]
            interpretation = send(prompt)
            return interpretation

    def _decide(self):
        self.interpretation = self._interpret()
        prompt = f"""
Based on the the interpretation below ({self.interpretation}) that you your made make a decision based on the current state {self.state}, 
that will lead you closest to you defined goal({self.goal})
"""

        decision = send(prompt)
        return decision

    def memory(self):
        prompt = f"""
from the interpretation: {self.interpretation} you made earlier remove what is important for you to remember and will help you to learn something, outline them in points.
        """
        memory = send(prompt)
        return memory
