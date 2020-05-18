from .Person import Person


class Student(Person):
    """
    Classe que representa a tabela Student
    """

    def __init__(self, code="", name="", email="", punctuation=None):
        super().__init__(name)
        self.code = code
        self.email = email
        self.punctuation = punctuation
        self.average = 0
        self.situation = ''

    def __repr__(self):
        self.generate_situation()
        return "Nome: {}\nNotas: {}, {}, {}\nMédia: {}\nSituação: {}".format(
            self.name,
            self.punctuation[0],
            self.punctuation[1],
            self.punctuation[2],
            self.average,
            self.situation
        )

    def calculation_average(self):

        return sum(self.punctuation)/len(self.punctuation)

    def calculation_situation(self):
        if self.average >= 7:
            return "Aprovado"
        return "Reprovado"

    def generate_situation(self):
        self.average = self.calculation_average()
        self.situation = self.calculation_situation()

    def is_aproved(self):
        self.generate_situation()
        if self.situation == "Aprovado":
            return True
        return False
