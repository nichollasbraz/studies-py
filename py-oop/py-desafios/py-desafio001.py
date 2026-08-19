from rich import print
from rich import inspect

class Funcionario():
    empresa = "Havan S.A"

    def __init__(self, nome = "desconhecido", setor = "desconhecido", cargo = "desconhecido"):
        self.id = nome
        self.ramo = setor
        self.posto = cargo

    def __str__(self):
        if self.id == "desconhecido" and self.ramo == "desconhecido" and self.posto == "desconhecido":
            return f"funcionário desconhecido."
        else:
            return f"olá! me chamo {self.id}, trabalho no setor {self.ramo} como {self.posto} na empresa {self.__class__.empresa}."


f1 = Funcionario("Thalys Nogueira da Silva", "Logístico", "Conferente")

print(f1)
inspect(f1)
inspect(Funcionario())
        