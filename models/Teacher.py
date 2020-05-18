from .Person import Person


class Teacher(Person):
    """
    Classe que representa a tabela Professor
    """

    seq = 0
    objects = []

    def __init__(self, name=""):
        super().__init__(name)

    def save(self):
        self.__class__.seq += 1
        self.id = self.__class__.seq
        self.__class__.objects.append(self)

    @classmethod
    def get_or_create(cls, string):
        for item in cls.objects:
            if string.lower() == item.name.lower():
                return item
        teacher = Teacher(name=string)
        return teacher

    @classmethod
    def all(cls):
        if len(cls.objects) == 0:
            print("Não possui itens cadastradas.")
        for item in cls.objects:
            print(item)
