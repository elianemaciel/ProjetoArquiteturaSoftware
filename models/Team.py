from .Discipline import Discipline
from .Teacher import Teacher


class Team(object):
    """
    Classe que representa a tabela Turma
    """

    def __init__(self, code="", discipline=Discipline(), teacher=Teacher()):
        self.id = None
        self.code = code
        self.discipline = discipline
        self.teacher = teacher
        self.students = []

    def __repr__(self):
        return """
            Código da turma: {}\n
            Nome da Disciplina: {}\n
            Nome do Professor {}\n
            Quantidade de alunos: {}\n""".format(
                self.code,
                self.discipline.name,
                self.teacher.name,
                len(self.students)
            )

    def add_student(self, student):
        self.students.append(student)

    def show_students(self):
        for student in self.students:
            print(student)

    def calc_approved(self):
        approved = 0
        for student in self.students:
            if student.is_aproved():
                approved += 1
        return approved

    def calc_percent_approved(self, approved):
        return approved/len(self.students) * 100
