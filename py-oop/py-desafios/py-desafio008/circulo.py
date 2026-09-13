from poligono import Poligono

class Circulo(Poligono):
    def __init__(self, diametro = 1):
        self.raio = diametro / 2

    def perimetro(self):
        self.perimetroResult = 2 * 3.14 * self.raio
        return f"perímetro do círculo: {self.perimetroResult:.2f}"

    def area(self):
        self.areaResult = 3.14 * (self.raio ** 2)
        return f"área do círculo: {self.areaResult:.2f}"
    