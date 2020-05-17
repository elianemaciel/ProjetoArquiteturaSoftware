from .Pessoa import Pessoa


class Aluno(Pessoa):
    """
    Classe que representa a tabela Aluno
    """

    def __init__(self, codigo="", nome="", email="", notas=None):
        super().__init__(nome)
        self.codigo = codigo
        self.email = email
        self.notas = notas
        self.media = 0
        self.situacao = ''

    def __repr__(self):
        self.gera_situacao()
        return "Nome: {}\nNotas: {}, {}, {}\nMédia: {}\nSituação: {}".format(
            self.nome,
            self.notas[0],
            self.notas[1],
            self.notas[2],
            self.media,
            self.situacao
        )

    def calcula_media(self):

        return sum(self.notas)/len(self.notas)

    def calcula_situacao(self):
        if self.media >= 7:
            return "Aprovado"
        return "Reprovado"

    def gera_situacao(self):
        self.media = self.calcula_media()
        self.situacao = self.calcula_situacao()

    def is_aproved(self):
        self.gera_situacao()
        if self.situacao == "Aprovado":
            return True
        return False
