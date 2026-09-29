from abc import ABC, abstractmethod

class Funcionario(ABC):

    def __init__(self, nome: str, salario: float = 1621):
        self._nome = nome
        self.__salario = salario


    def __str__(self) -> str:
        return (
            f"{self._nome} atua como {self.__class__.__name__}.\n"
            f"{self._nome} recebe R${self.__salario:,.2f} de salário.\n"
            f"{self._nome} recebe R${self.avaliar_bonus():,.2f} de bônus."
            )

    @abstractmethod
    def avaliar_bonus(self):
        pass


    @property
    def salario(self):
        return self.__salario


    @salario.setter
    def salario(self, valor: float = None) -> float:
        if valor is None:
            raise ValueError("não é possível alterar o valor desta maneira.")
        else:
            if valor >= self.__salario:
                self.__salario = valor
            else:      
                raise ValueError("novo salário não pode ser menor que o anterior.")


class Designer(Funcionario):

    def avaliar_bonus(self):
        return self.salario * 0.08


class Gerente(Funcionario):

    def avaliar_bonus(self):
        return self.salario * 0.15


class Desenvolvedor(Funcionario):

    def avaliar_bonus(self):
        return self.salario * 0.10
