from abc import ABC, abstractmethod # Abstract Base Classes

class Pessoa(ABC):
    escola = "Colégio Curso em Vídeo"

    def __init__(self, nome = "null", idade = 0):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1
        return f"{self.nome} fez aniversário! ele(a) fez {self.idade} anos."

    @abstractmethod
    def estudar(self):
        pass
    