from classes import *

def main():
    try:
        funcionarios = [
            Gerente("Marcos Alexandre", 16_000),
            Desenvolvedor("Ana Lúcia", 12_000),
            Designer("Nichollas Bras", 8_000)
            ]

        for funcionario in funcionarios:
            print(funcionario)

    except Exception as e:
        print(f"erro ({e.__class__.__name__}): {e}")


if __name__ == "__main__":
    main()
