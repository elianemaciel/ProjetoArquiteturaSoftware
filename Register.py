#!/usr/bin/env python3

from models.Discipline import Discipline
from models.Teacher import Teacher
from models.Student import Student
from models.Team import Team


class Register(object):
    """
    Padrões Façade
    """

    def register_discipline(self, discipline):
        return Discipline.get_or_create(discipline)

    def register_teacher(self, teacher):
        return Teacher.get_or_create(teacher)

    def register_turma(self, composite):
        print("Dados para a turma: ")
        code = input("Digite o código da turma: ")
        name = input("Digite o nome do professor: ")
        discipline_str = input("Digite o discipline: ")
        discipline = self.register_discipline(discipline_str)
        teacher = self.register_teacher(name)

        turma = Team(
            code=code,
            discipline=discipline,
            teacher=teacher
        )
        composite.add(turma)

        return turma

    def register_student(self, composite):

        print("Dados do aluno: ")
        code = input("Digite o código: ")
        name = input("Digite o nome do aluno: ")
        email = input("Digite o e-mail: ")
        punctuation = input("Digite as 3 notas separadas por vírgola: ")
        list_punctuation = [int(x) for x in punctuation.split(",")]

        student = Student(
            code=code,
            name=name,
            email=email,
            punctuation=list_punctuation
        )
        composite.add(student)
        return student
