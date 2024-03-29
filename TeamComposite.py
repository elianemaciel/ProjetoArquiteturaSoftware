#!/usr/bin/env python3
from models.Team import Team


class TeamComposite(Team):

    def __init__(self):
        self._children = []

    def add(self, turma):
        self._children.append(turma)

    def show_all(self):
        if len(self._children) == 0:
            print("Não possui itens cadastradas.")
        for item in self._children:
            print(item)

    def get(self, string):
        for item in self._children:
            if string.lower() == item.code.lower():
                return item

    def show_all_detail(self):
        for item in self._children:
            approved = item.calc_approved()
            percent_approved = item.calc_percent_approved(approved)
            print(item)
            print("""
                Número de aprovados: {}
                Percentual de Aprovados: {}""".format(
                    approved,
                    percent_approved
                )
            )
