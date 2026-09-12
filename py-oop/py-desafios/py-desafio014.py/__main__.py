from classes import *

def main():
    d = Diario()
    d.escrever = "eu te amo"
    d.escrever = "sou Thalys"
    d.escrever = "nogueira"
    d.ler = "CeV!@"

    try:
        print(d.ler)
    except Exception as e:
        print(f"erro: {e}")

if __name__ == "__main__":
    main()