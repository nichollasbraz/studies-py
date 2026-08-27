from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def matricula(self):
        return f"o aluno {self.nome} acabou de matricular-se no {self.escola}."
