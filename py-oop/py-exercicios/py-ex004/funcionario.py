from pessoa import Pessoa

class Funcionario(Pessoa):
    def estudar(self):
        pass

    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def ponto(self):
        return f"a funcionária {self.nome} iniciou sua jornada diária como {self.cargo}."
