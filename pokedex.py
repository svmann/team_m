import json

from linkedlist import LinkedList
from pokemon import Pokemon

class Pokedex(object):

        def __init__(self):
            pass

        def run(self):
            try:
                poke_list = LinkedList()
                with open("pokedex.json", "r") as file:
                    data = json.load(file)

                for poke in data:
                    
                    pokemon = Pokemon(poke['id'], poke['name'], poke['types'], poke['evolves_into'])
                    poke_list.add(pokemon)
                print(poke_list)

            except IOError:
                print("Error: pokedex.json file does not exist.")
                return


if __name__ == "__main__":
    Pokedex().run()
