from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0

    @abstractmethod

    def calc_frete(self):
        pass
    