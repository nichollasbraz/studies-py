from classes import *

def main():

    cc = ContaBancaria(111, "thalys", 10_000)
    cc.saque(500)
    cc.titular = "Nogueirão"

if __name__ == "__main__":
    main()
    