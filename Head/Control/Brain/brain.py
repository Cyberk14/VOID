# this will be used to process the input from the "Input" folder for storage, re-use and output!
from .memory import previous_5
import utils
from Head.Input.ears import listen
from Head.Input.eyes import see

from typing import List, Dict, Literal, Any
from termcolor import colored



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
        # info = eye()
        self.message = listen()
        
        self.state = state()
        self.goal = f"Briefly and concisely define the goal of the prompt below \n {self.message}"

    def interpret(self, image: str|None=None):
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
            interpretation = send_img(prompt, image)
            print(colored(interpretation, 'green'))
            return interpretation

    def decide(self):
        self.interpretation = self.interpret()
        prompt = f""" 
    Based on the provided self.message and your interpretation that you made, make a decision considering the following:
    User/Fellow Agent's self.Message: "{self.message}"
    Your Interpretation: "{self.interpretation}"
    
    Display the decision as follows:
    'Decision: ``I have decided that (decision_goes_here)``'
    """

        decision = utils.send_str(prompt)
        
        print(colored(decision, "red"))
        return decision

    def respond(self) -> tuple[str, Any, Any, Any]:
        decision = self.decide()
        prompt = f"""
You received the following prompt: "{self.message}".
You interpreted it as: "{self.interpretation}".
Based on this interpretation and the prompt, you decided: "{decision}".
if you dont know something or a fact dont print it!!!!! 

Now, please respond as human, naturally as if you are talking to a human companion/friend. Adopt to slang speech pattern. Here is your response:
"""

        response = utils.send_str(prompt)
        print(colored(response, 'blue'))
        
        conversation = utils.conv_cont(self.message, self.interpretation, decision, response)
        # utilities.text_to_speech_file(response)
        previous_5(True)
        
        return conversation
