import json

from linkedlist import LinkedList
from pokemon import Pokemon

class Pokedex(object):

        def __init__(self):
            pass

        def run(self):
            try:
                with open("pokedex.json", "r") as file:
                    data = json.load(file)

                print(json.dumps(data))

            except IOError:
                print("Error: pokedex.json file does not exist.")
                return


if __name__ == "__main__":
    Pokedex().run()
