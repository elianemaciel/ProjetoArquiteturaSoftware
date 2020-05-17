from .Pessoa import Pessoa


class Professor(Pessoa):
    """
    Classe que representa a tabela Professor
    """

    seq = 0
    objects = []

    def __init__(self, nome=""):
        super().__init__(nome)

    def save(self):
        self.__class__.seq += 1
        self.id = self.__class__.seq
        self.__class__.objects.append(self)

    @classmethod
    def get_or_create(cls, string):
        for item in cls.objects:
            if string.lower() == item.name.lower():
                return item
        professor = Professor(nome=string)
        return professor

    @classmethod
    def all(cls):
        if len(cls.objects) == 0:
            print("Não possui itens cadastradas.")
        for item in cls.objects:
            print(item)
