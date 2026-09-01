from abc import ABC, abstractmethod
from time import sleep

class BebidaQuente(ABC):
    def prepararBebida(self):
        self.selecionarBebida()
        self.ferverAgua()
        sleep(1)
        self.misturarBebida()
        sleep(1)
        self.servirBebida()
        sleep(1)
        print("pronto para consumo.")
        sleep(1)
        print()

    def ferverAgua(self):
        print("fervendo água...")

    @abstractmethod
    def selecionarBebida(self):
        pass

    @abstractmethod
    def misturarBebida(self):
        pass

    @abstractmethod
    def servirBebida(self):
        pass


class Cafe(BebidaQuente):
    def selecionarBebida(self):
        print("bebida selecionada: café.", end=" ")

    def misturarBebida(self):
        print("passando água pressurizada pelo pó de café moído...")
        
    def servirBebida(self):
        print("servindo em xícara pequena...")


class Cha(BebidaQuente):
    def selecionarBebida(self):
        print("bebida selecionada: chá.", end=" ")

    def misturarBebida(self):
        print("mergulhando sachê de ervas na água...")

    def servirBebida(self):
        print("servindo em caneca de porcelana com limão...")
        

class Leite(BebidaQuente):
    def selecionarBebida(self):
        print("bebida selecionada: leite.", end=" ")

    def misturarBebida(self):
        print("passando água pressurizada no bico do leite...")

    def servirBebida(self):
        print("servindo na caneca grande, já com café...")

