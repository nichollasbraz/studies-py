from transporte import Transporte
from time import sleep

class Moto(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.frete = 0.5

    def calc_frete(self):
        via = Moto(self.distancia)
        via = type(via).__name__.lower()

        self.freteResult = self.frete * self.distancia
        print(f"frete selecionado: {via}. alíquota logística: r${self.frete:.2f}.")
        sleep(1.5)
        print(f"preço estimado de {self.distancia}km via {via}: r${self.freteResult:.2f}.")
        sleep(1.5)
        print()
