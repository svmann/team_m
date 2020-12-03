from typing import Iterable


class Pokemon():
    def __init__(self, id: int, name: str, types:  Iterable, evolutions: Iterable):
        self.id = id
        self.name = name
        self.types = types
        self.evolutions = evolutions


    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name

    def get_types(self):
        return self.types


    def get_evolutions(self):
        return self.evolutions


