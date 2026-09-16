from abc import ABC

class Mom(ABC):

    def __init__(self, nome: str = ""):
        self.nome = nome.lower()


    def fritarCoxinha(self):
        print(
            f"{self.nome} frita coxinha por imersão no óleo."
        )


    def fazerPudim(self):
        print(
            f"{self.nome} faz pudim de forno em banho-maria."
        )


class Son(Mom):

    def fritarCoxinha(self):
        print(
            f"{self.nome} frita coxinha na airfryer."
        )


    def fazerPudim(self):
        print(
            f"{self.nome} faz pudim na boca do fogão."
        )
class Daughter(Mom):

    def fazerPudim(self):
        print(
            f"{self.nome} faz pudim de micro-ondas."
        )


    def fritarCoxinha(self):
        print(
            f"{self.nome} prefere assar coxinha, no forno."
        )
