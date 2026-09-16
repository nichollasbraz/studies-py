from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, nome):
        self.nome = nome


    def emitirSom(self):
        print(
            f"{self.nome} é um(a) {self.__class__.__name__.lower()} e está emitindo um som."
            )


class Cachorro(Animal):

    def emitirSom(self):
        print(
            f"{self.nome} diz: Au, Au, Au!"
            )


class Spitz(Cachorro):

    def emitirSom(self):

        print(
            f"{self.nome} diz: au, au, au, au!"
        )
    

class Pitbull(Cachorro):

    def emitirSom(self):
        print(
            f"{self.nome} diz: RUF! RUF!"
        )
        
class Gato(Animal):

    def emitirSom(self):
        print(
            f"{self.nome} diz: meOoOoOw!"
        )


class Pato(Animal):

    def emitirSom(self):
        print(
            f"{self.nome} diz: quack, quack!"
        )


class Galinha(Animal):

    def emitirSom(self):
        print(
            f"{self.nome} diz: CoCó!"
        )

