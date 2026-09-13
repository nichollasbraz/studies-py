from classes import *

s = SHA256()

def main():

    try:
        s.senha = '323'
        print(s.senha)
        s.validar('323')
    except Exception as e:
        print(f"houve um erro: {e}")


if __name__ == "__main__":
    main()
    