# this will be used to process the input from the "Input" folder for storage, re-use and output!


import tools
from Head.Input.ears import listen
from Head.Input.eyes import see
from . import memory

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

    def decide(self):
        if self.message == '':
            print('Good bye...')
            
            print(f"message: {self.message}")

            with open('previous_five.txt', 'r') as file:
                text = file.read()

            knowledge = tools.knowledge_graph(text)

            memory.long_term_mem(knowledge, switch=True)


            print(knowledge_graph)
            sys.exit()
            return None

        prompt = f""" 
Based on the provided self.message, make a decision considering the following:
User/Fellow Agent's self.Message: "{self.message}"

In this stage is where tools are used then there response is gathered.

here are the tools {memory.utils.Youtube.register(), utils.Search.register()} read the ``description`` and follow the ``how to``, let's think step by step

- Call the tool displaying there how_to according argument
- Display only the decision nothing else.

Decision: """

        decision = utils.send_str(prompt)
        print(colored(decision, "red"))

        results = utils.action(decision)
        return decision, results

    def respond(self) -> tuple[str, Any, Any, Any]:
        decision, results = self.decide()
        
        if results:
            
            print('tool used')
            
            prompt = f"""
You received the following prompt: "{self.message}".
Based on this interpretation and the prompt, you decided: "{decision}".
if you don't know something or a fact don't print it!!!!! 

explain this in detail: {results}
Here's your response:
    """
            response = utils.send_str(prompt)
            print(colored(response, 'blue'))
            
            conversation = utils.conv_cont(self.message, decision, response)
            utils.text_to_speech_file(response)
            
            return conversation
        
        print('tool not used...')

        prompt = f"""
        You received the following prompt: "{self.message}".
Based on this interpretation and the prompt, you decided: "{decision}".
if you don't know something or a fact don't print it!!!!! 

Here's your response:
        """

        response = utils.send_str(prompt)
        print(colored(response, 'blue'))
        
        conversation = utils.conv_cont(self.message, decision, response)
        utils.text_to_speech_file(response)
        
        return conversation
