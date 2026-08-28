from poligono import Poligono

class Quadrado(Poligono):
    def __init__(self, lados, comprimento):
        super().__init__(lados)
        self.comprimento = comprimento

    def perimetro(self):
        self.perimetroResult = self.comprimento * 4
        return f"perímetro do quadrado: {self.perimetroResult}"

    def area(self):
        self.areaResult = self.comprimento ** 2
        return f"área do quadrado: {self.areaResult}"
    