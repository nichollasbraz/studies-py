from abc import ABC, abstractmethod
from time import sleep

class Funcionario(ABC):
    salMin = 1621
    contSalMin = 0 
    cotInss = 0.075

    def __init__(self, nome = "", salario = 0):
        self.nome = nome
        self.salario = salario


    def analisarSal(self):
        tipoFunc = type(self).__name__.lower()
        self.contSalMin = self.calcSal() / self.salMin

        print(f"salário mínimo : r${self.salMin:,.2f}. alíquota do INSS : %{self.cotInss * 100}. calculando salário...")
        sleep(1.2)
        print(f"salário líquido de {self.nome} ({tipoFunc}) : r${self.calcSal():,.2f}.")
        sleep(1.2)
        print(f"salário líquido corresponde a {self.contSalMin:.1f} salários mínimos.")
        sleep(1.2)
        print()


    @abstractmethod
    def calcSal(self):
        pass


class Horista(Funcionario):
    def __init__(self, nome, valorHora, totHoras):
        super().__init__(nome)
        self.valorHora = valorHora
        self.totHoras = totHoras


    def calcSal(self):
        self.salBruto = (self.totHoras * self.valorHora)
        self.salLiq = self.salBruto - (self.cotInss * self.salBruto)
        return self.salLiq


class Mensalista(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)


    def calcSal(self):
        self.salLiq = self.salario - (self.cotInss * self.salario) 
        return self.salLiq
