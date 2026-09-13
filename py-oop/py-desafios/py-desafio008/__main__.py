from quadrado import Quadrado
from circulo import Circulo

def main():
    q = Quadrado(4, 5)

    print(q.area())
    print(q.perimetro())

    c = Circulo(5)

    print(c.perimetro())
    print(c.area())

if __name__ == "__main__":
    main()
