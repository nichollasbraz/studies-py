from classes import *

def main():
    t = Thermo()

    try:
        t.temperatura = 21
    except Exception as e:
        print(f"houve um problema: {e}")

    print(t.temperatura)


if __name__ == "__main__":
    main()