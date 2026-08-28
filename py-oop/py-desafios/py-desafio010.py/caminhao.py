from transporte import Transporte
from time import sleep

class Caminhao(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.frete = 1.2

    def calc_frete(self):
        if self.distancia < 50:
            print(f"distância mínima do caminhão: 50km.")
            sleep(1.5)
            print()
        else:
            self.freteResult = self.frete * self.distancia
            print(f"frete selecionado: caminhão. alíquota logística: r${self.frete:.2f}.")
            sleep(1.5)
            print(f"preço estimado de {self.distancia}km via caminhão: r${self.freteResult:.2f}.")
            sleep(1.5)
            print()
