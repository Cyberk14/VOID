from Head.Control.Brain.brain import Brain
from Head.Output.mouth import speak


if __name__ == "__main__":
    while True:
        try:
            xenia = Brain()
            xenia.respond()
            speak()
        except Exception as error:
            print('An error occurred: ', error)
