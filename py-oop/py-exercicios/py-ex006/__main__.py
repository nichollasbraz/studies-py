from ex006 import *

def main():
    al_1 = Avaliacao("Pedro", "Matemática")
    print(al_1.__dict__)
    print(al_1.set_nota(10))
    print(al_1.__dict__)


if __name__ == "__main__":
    main()