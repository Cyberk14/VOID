# this will be used to process the input from the "Input" folder for storage, re-use and output!
from .memory import update
import utils
from Head.Input.ears import listen
from Head.Input.eyes import see

from typing import Any
from termcolor import colored
import sys



def state():# -> Any:
    prompt = """
    ``These is a prompt made specifically to let you be aware for you current and Previous BUT only the last five states will be given to you to save time and space``
    
    Previous Dialogue: {dialogue} \\

    Previous Actions: {actions} \\
    """
    
    state = utils.send_str(prompt)
    return state

class Brain:
    def __init__(self):
        self.message = listen()
        self.goal = f"Briefly and concisely define the goal of the prompt below \n {self.message}"

    def interpret(self, image: str|None=None):
        if not self.message:
            print('Goodbye')
            sys.exit()
        
        else:
            prompt = f"""
            You have received this self.message interpret it and understand its core values and meanings: "{self.message}"
            
            Summarize the content in bullet points or in a clear and concise format, ensuring it retains its original meaning and value.
            
            Display the interpretation as follows:
            'Interpretation: ``Based on (this) or (that) I interpreted as (interpretation_goes_here)``'
            """

            if not image:
                interpretation = utils.send_str(prompt)
                print(colored(interpretation, 'green'))
                return interpretation
            else:
                interpretation = utils.send_img(prompt, image)
                print(colored(interpretation, 'green'))
                return interpretation

    def decide(self):
        self.interpretation = self.interpret()
        prompt = f""" 
Based on the provided self.message and your interpretation that you made, make a decision considering the following:
User/Fellow Agent's self.Message: "{self.message}"
Your Interpretation: "{self.interpretation}"

In this stage is where tools are used then there response is gathered.

here are the tools {utils.Youtube.register(), utils.Search.register()} read the ``description`` and follow the ``how to``, let's think step by step

- Call the tool displaying there how_to according argument

display decision as follows:
Decision:``i have decided that``"""

        decision = utils.send_str(prompt)
        print(colored(decision, "red"))
        results = utils.action(decision)
        return decision, results

    def respond(self) -> tuple[str, Any, Any, Any]:
        decision, results = self.decide()
        prompt = f"""
You received the following prompt: "{self.message}".
You interpreted it as: "{self.interpretation}".
Based on this interpretation and the prompt, you decided: "{decision}".
if you dont know something or a fact dont print it!!!!! 

Incase you used any tool here's the data from the tool: {results} |||| elaborate more on the data.

Here's your response:
"""

        response = utils.send_str(prompt)
        print(colored(response, 'blue'))
        
        conversation = utils.conv_cont(self.message, self.interpretation, decision, response)
        # utils.text_to_speech_file(response)
        update(True)
        
        return conversation
