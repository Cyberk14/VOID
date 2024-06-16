from Head.Control.Brain.brain import Brain

if __name__ == '__main__':
    agent = Brain()
    print(agent.interpret())
    print(agent.decide())

