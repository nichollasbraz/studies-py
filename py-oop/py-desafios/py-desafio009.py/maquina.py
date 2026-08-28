from abc import ABC, abstractmethod
from time import sleep

class Maquina(ABC):
    def __init__(self):
        pass

    def ferverAgua(self):
        return f"fervendo água..."

    def preparar(self):
        print(f"iniciando preparo...")
        sleep(1.5)
        print(f"{self.ferverAgua()}")
        sleep(1)
        print(f"{self.misturar()}")
        sleep(1)
        print(f"{self.servir()}")
        sleep(1)
        print("pronto para consumo.")
        sleep(1)
        print()
        
    @abstractmethod

    def misturar(self):
        pass

    def servir(self):
        pass
        