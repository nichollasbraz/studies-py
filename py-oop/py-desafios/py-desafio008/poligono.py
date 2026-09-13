from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, lados = 1):
        self.qtdLados = lados

    @abstractmethod

    def perimetro(self):
        pass

    def area(self):
        pass