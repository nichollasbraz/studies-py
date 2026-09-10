from classes import *

def main():
    c1 = ContaBancaria(112, "Gustavo Guanabara", 3000)
    c1.saldo = 0
    print(c1.saque(+1000))
    print(c1.deposito(-700))
    c1.titular = "Pedro"
    print(c1)


if __name__ == "__main__":
    main()