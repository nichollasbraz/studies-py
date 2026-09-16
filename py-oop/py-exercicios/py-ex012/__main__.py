from classes import *

def main():
    try:
        c = Carteira(1000)
        c2 = Carteira(2000)

        c += 50
        c -= 200

        if (c <= c2):
            print("a primeira carteira tem mais dinheiro.")
        else:
            print("a segunda carteira tem mais dinheiro.")


    except Exception as e:
        print(f"erro({e.__class__.__name__}): {e}")


if __name__ == "__main__":
    main()
    