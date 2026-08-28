from moto import Moto
from drone import Drone
from caminhao import Caminhao

def main():
    b = Moto(20)
    b.calc_frete()

    d = Drone(10)
    d.calc_frete()

    d = Drone(11)
    d.calc_frete()

    c = Caminhao(49)
    c.calc_frete()
    c = Caminhao(120)
    c.calc_frete()

if __name__ == "__main__":
    main()
    