from Head.Control.Brain.brain import Brain
from Head.Output.mouth import speak

if __name__ == '__main__':
    model = Brain()
    
    speak(model.respond())
