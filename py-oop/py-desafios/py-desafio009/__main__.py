from cafe import Cafe
from leite import Leite
from cha import Cha

def main():
    c = Cafe()
    c.preparar()

    l = Leite()
    l.preparar()

    ch = Cha()
    ch.preparar()

if __name__ == "__main__":
    main()
