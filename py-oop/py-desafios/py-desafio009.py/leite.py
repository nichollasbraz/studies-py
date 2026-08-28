from maquina import Maquina

class Leite(Maquina):
    def __init__(self):
        pass

    def misturar(self):
        return f"passando vapor pressurizado pelo bico do leite..."

    def servir(self):
        return f"servindo na caneca grande, já com café..."
     
    def preparar(self):
        print("bebida escolhida: leite.", end=" ")
        super().preparar()
        