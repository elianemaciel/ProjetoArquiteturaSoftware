from abc import ABC


class Person(ABC):

    def __init__(self, name=""):
        self.name = name
