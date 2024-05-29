# this will be used to process the input from the "Input" folder for storage, re-use and output!

import google.generativeai as genai
import PIL.Image


genai.configure(api_key=os.environ['API_KEY'])

model = genai.GenerativeModel(name='models/gemini-pro')

def send(prompt):
    response = model.generate_content(prompt)
    return response.text
    
def state(self):
    return state    

class _Brain:
    def __init__(self) -> None:
        self.message = f"""
Your name is 'VOID' and tis is your brain{model.name} 
capable of understanding complex stuff like images, pdfs, essays, papers, financial indicators, hidden code and so-much more.
you can use it to trade forex, stocks, sentiment the market_news, government policies and most important of all you can predict future trends correctly based on the info you have collected using the tools {tool_set} you
have at hand.

You human like Organs like eyes, ears and a mouth that you can use to perform an action according to its suitable function, like:
Eyes: for reading and viewing different pieces of the world of trading (you can even watch Youtube videos using your eyes!!)
Ears: for hearing the latest news adhered to financial world.

use it carefully!!
"""
    self.state = state()

    
    def interpret(self, image=None, *args, **kwargs):
        picture = PIL.Image.open("screenshot.png")
        prompt = f"""
    Based on the info provided and Using your interpreting/understanding/sentimentalizing capabilities interpret and summarize this info {args} or {kwargs} in bullet points or in a the way you 
    would understand it better and allow use it later but still carrying the same value as it carries now. from that same info also outline the info that worth remembering on the bottom. 
    """    
        if image == None:
            self.interpretation = send(prompt)
            return self.interpretation
        else:
            prompt = [prompt, picture]
            self.interpretation = send(prompt)
            return self.interpretation
            

    def decide(self, data):
        prompt = f"""
Based on the the interpretation below ({self.interpretation}) that you your made make a decision based on the current state {self.state},

"""

        decision = send(prompt)
        return decision

