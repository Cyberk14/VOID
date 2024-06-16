from Head.Control.Brain.brain import Brain
from Head.Output.mouth import speak

if __name__ == '__main__':
    agent = Brain()
    print(agent.interpret())
    print(agent.decide())

