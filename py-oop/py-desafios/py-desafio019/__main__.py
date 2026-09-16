from classes import *

def main():

    try:
        p = Aluno("Gustavo", 1995, "ADM")
        print(p.idade)
        print(p.add_curso("NOGUEIRA"))
        p.curso = "NOGUEIRA"
        print(p.__dict__)
        print(p.curso)

    except Exception as e:
        print(f"erro: {e}")


if __name__ == "__main__":
    main()
