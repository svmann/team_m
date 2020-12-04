from typing import Iterable


class Pokemon():
    def __init__(self, id: int, name: str, types:  Iterable, evolutions: Iterable):
        self.id = id
        self.name = name
        self.types = types
        self.evolutions = evolutions

    def __str__(self):
        return_string = "ID: " + str(self.id) + "\n Name: " + self.name + "\n Types: " + str(self.types) + "\n Evolves into: " + str(self.evolutions) + "\n"
        return return_string


