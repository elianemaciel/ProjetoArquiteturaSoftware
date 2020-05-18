#!/usr/bin/env python3

from Register import Register
from TeamComposite import TeamComposite
from StudentComposite import StudentComposite


class MenuOptions:
    """
    Padrão de Criação Singleton
    O método classmethod instance() verifica se já existe uma instância da classe e caso não exista, ele cria essa instância e retorna para o usuário.
    """

    _instance = None

    def __init__(self):
        self.composite = TeamComposite()
        self.composite_student = StudentComposite()

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def show_menu(self):
        print("------------------------------------------------------------\n")
        print("                   Instituição TI                           \n")
        print("------------------------------------------------------------\n")
        print("Escolha uma das opções a seguir:\n")
        print(" 1) Listar todas as Turma\n")
        print(" 2) Informar dados de uma turma\n")
        print(" 3) Consultar os dados de uma turma\n")
        print(" 4) Consultar estatísticas gerais\n")
        print(" 5) Sair do sistema\n")
        print("------------------------------------------------------------\n")

    def option_one(self):
        self.composite.show_all()

    def option_two(self):
        register = Register()
        turma = register.register_turma(self.composite)

        option = 'S'

        while option.upper() == "S":
            student = register.register_student(self.composite_student)
            turma.add_student(student)
            option = input('Deseja cadastrar novo aluno? ')

    def option_three(self):
        code = input("Digite o código da turma: ")
        turma = self.composite.get(code)
        print(turma)
        turma.show_students()

    def option_four(self):
        self.composite.show_all_detail()
        total, approved, percent = self.composite_student.statistics()
        print(
            """
            Total de alunos na instituição: {}
            Total de aprovados: {}
            Percentual de Aprovados: {}""".format(
                total,
                approved,
                percent
            )
        )
