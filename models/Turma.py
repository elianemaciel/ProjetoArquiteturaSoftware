from .Disciplina import Disciplina
from .Professor import Professor


class Turma(object):
    """
    Classe que representa a tabela Turma
    """

    def __init__(self, codigo="", disciplina=Disciplina(), professor=Professor()):
        self.id = None
        self.codigo = codigo
        self.disciplina = disciplina
        self.professor = professor
        self.alunos = []

    def __repr__(self):
        return """
            Código da turma: {}\n
            Nome da Disciplina: {}\n
            Nome do Professor {}\n
            Quantidade de alunos: {}\n""".format(
                self.codigo,
                self.disciplina.name,
                self.professor.nome,
                len(self.alunos)
            )

    def add_aluno(self, aluno):
        self.alunos.append(aluno)

    def show_alunos(self):
        for aluno in self.alunos:
            print(aluno)

    def calc_aprovados(self):
        aprovados = 0
        for aluno in self.alunos:
            if aluno.is_aproved():
                aprovados += 1
        return aprovados

    def calc_percent_aprovados(self, aprovados):
        return aprovados/len(self.alunos) * 100
