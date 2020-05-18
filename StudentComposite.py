#!/usr/bin/env python3

from models.Student import Student


class StudentComposite(Student):

    def __init__(self):
        self._children = []

    def add(self, student):
        self._children.append(student)

    def show_all(self):
        if len(self._children) == 0:
            print("Não possui itens cadastradas.")
        for item in self._children:
            print(item)

    def statistics(self):
        total = len(self._children)
        approved = 0
        for student in self._children:
            if student.is_aproved():
                approved += 1
        percert = approved / total * 100

        return total, approved, percert
