from maquina import Maquina

class Cafe(Maquina):
    def __init__(self):
        pass

    def misturar(self):
        return f"passando água pressurizada pelo pó de café moído..."

    def servir(self):
        return f"servindo em xícara pequena..."

    def preparar(self):
        print("bebida escolhida: café.", end=" ")
        super().preparar()

        