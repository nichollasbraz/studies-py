from maquina import Maquina

class Cha(Maquina):
    def __init__(self):
        pass

    def misturar(self):
        return f"mergulhando chá de ervas na água..."

    def servir(self):
        return f"servindo na caneca de porcelana com limão..."

    def preparar(self):
        print("bebida escolhida: chá.", end=" ")
        super().preparar()
