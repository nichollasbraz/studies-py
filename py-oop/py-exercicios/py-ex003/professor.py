from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, idade, nivel, materia):
        super().__init__(nome, idade)
        self.materia = materia
        self.nivel = nivel

    def aula(self):
        return f"o professor {self.nome} começou sua aula de {self.materia}."
    