from classes import *

def main():

    r = Retangulo()
    try:
        
        r.medidas = (5.3, 2.3)
        print(r.medidas)
    except Exception as e:
        print(f"ocorreu um erro ({type(e).__name__}): {e}")


if __name__ == "__main__":
    main()
