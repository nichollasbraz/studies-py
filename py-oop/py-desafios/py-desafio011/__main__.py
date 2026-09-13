from classes import *

def main():
    func1 = Horista("Paulo Guina", 50, 220)

    func1.calcSal()
    func1.analisarSal()

    func2 = Mensalista("Jailson Mendes", 21950)
    func2.calcSal()
    func2.analisarSal()


if __name__ == "__main__":
    main()
