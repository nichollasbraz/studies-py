from transporte import Transporte
from time import sleep

class Drone(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.frete = 9.5

    def calc_frete(self):
        if self.distancia > 10:
            print("distância máxima do drone: 10km.")
            sleep(1.5)
            print()
        else:
            self.freteResult = self.frete * self.distancia
            print(f"frete selecionado: drone. alíquota logística: r${self.frete:.2f}.")
            sleep(1.5)
            print(f"preço estimado de {self.distancia}km via drone: r${self.freteResult:.2f}.")
            sleep(1.5)
            print()
