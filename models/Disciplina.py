class Disciplina():
    """
    Classe que representa a tabela Disciplina
    """

    seq = 0
    objects = []

    def __init__(self, name=""):
        self.name = name

    def save(self):
        self.__class__.seq += 1
        self.id = self.__class__.seq
        self.__class__.objects.append(self)

    @classmethod
    def all(cls):
        if len(cls.objects) == 0:
            print("Não possui itens cadastradas.")
        for item in cls.objects:
            print(item)

    @classmethod
    def get_or_create(cls, string):
        for item in cls.objects:
            if string.lower() == item.name.lower():
                return item
        disciplina = Disciplina(name=string)
        disciplina.save()
        return disciplina
