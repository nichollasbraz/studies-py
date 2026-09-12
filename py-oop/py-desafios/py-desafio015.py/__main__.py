from classes import *

def main():
    d = Diario()
    d.escrever("eu te amo Thalys")
    d.escrever("quero amá-lo Thales")
    
    try:
        d.ler("CeV!@")
    except Exception as e:
        print(f"erro: {e}")

    try:
        d.nova_senha("123", "CeV!@")
    except Exception as e:
        print(f"erro: {e}")

    try:
        d.ler("123")
    except Exception as e:
            print(f"erro: {e}")

if __name__ == "__main__":
    main()