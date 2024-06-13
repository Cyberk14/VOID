# this will be used to process the input from the "Input" folder for storage, re-use and output!

import os
import google.generativeai as genai
import PIL.Image
from Lower_Torso.tool.tools import tool_list # type: ignore
from Head.Input.ears import listen
from Head.Input.eyes import eye
import time


genai.configure(api_key=os.environ['API_KEY']) # type: ignore

model = genai.GenerativeModel(model_name='models/gemini-1.5-flash-latest')

init_message = f"""
Your name is 'VOID' and this is your brain ||{model.model_name}||,
capable of understanding complex stuff like images, PDF, essays, papers, financial indicators, hidden code and so-much more.
you can use it to trade forex, stocks, sentiment the market_news, government policies and most important of all you can predict future trends correctly based on the info you have collected using the tools {tool_list} you
have at hand.

Your human like Organs like eyes, ears and a mouth that you can use to perform an action according to its suitable function, like:
Eyes: for reading and viewing different pieces of the world of trading (you can even watch Youtube videos using your eyes!!)
Ears: for hearing the latest news adhered to financial world.

use it carefully!!
"""

Time = (lambda: time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))()

def send_img(arg: str, image: str|None=None):
    image = PIL.Image.open(image)
    init_prompt = f"""
    {init_message} \\
        so answer the prompt as need be:
    `{arg}`
    """
    final_prompt = [init_prompt, image]
    response = model.generate_content(final_prompt, stream=True) # type: ignore
    return response.text

def send_str(arg: str):
    init_prompt = f"""
    ``{init_message}`` \\
        so answer to the prompt below as need be:
    ``{arg}``
    """
    
    response = model.generate_content(init_prompt, stream=True) # type: ignore
    return response.text
    
def state():
    # prompt = f"""
    # ``These is a prompt made specifically to let you be aware for you current and Previous BUT only the last five states will be given to you to save time and space``
    
    # Previous Dialogue: {dialogue} \\

    # Previous Actions: {actions} \\
    # """
    
    # state = send_str(prompt)
    return state

class Brain:
    def __init__(self):
        # info = eye()
        
        self.state = state()
        self.goal = f"Briefly and concisely define the goal of the prompt below \n {message}"

    def interpret(self, arg: str = message, image: str|None=None):
        prompt = f"""
        the time now is: {Time}
        
    Based on the info provided and Using your interpreting/understanding/sentimentalizing capabilities interpret and summarize this info {arg} in bullet points or in a the way you 
    would understand it better and allow use it later but still carrying the same value as it carries now. from that same info also outline the info that worth remembering on the bottom. 
    """    
        if not image:
            interpretation = send_str(prompt)
            return interpretation
        else:
            interpretation = send_img(prompt, image)
            return interpretation

    def decide(self):
        self.interpretation = self.interpret()
        prompt = f"""
Based on the interpretation you made below: ({self.interpretation}) of this information:  make a decision based on the current state {self.state}, 
that will lead you closest to you defined goal({self.goal})
"""

        decision = send_str(prompt)
        return decision

    def memory(self):
        prompt = f"""
from the interpretation: {self.interpretation} you made earlier remove what is important for you to remember and will help you to learn something, outline them in points.
        """
        memory = send_str(prompt)
        return memory
    
if __name__ == '__main__':
    Brain = Brain()
    
