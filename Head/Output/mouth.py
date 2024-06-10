# this will be more use-full to the user or assistant or even other like modeled agents to tell whats happening in reeal-time.TimeoutError

from Control.Brain.brain import Brain, send

Mind = Brain()
Thoughts = Mind.interpretation

def speak(self):
    prompt = f"""
from your thoughts -> {Thoughts} can you figure out what to say that is interesting, educating and important speak to your 
colleague that can help him learn of what have you done and wh did 
""" 



print(f"Thought: {Thoughts}")


