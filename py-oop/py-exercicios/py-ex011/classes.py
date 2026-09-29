from functools import singledispatchmethod

class Analisador:

    @singledispatchmethod
    def analisar(self, valor):
        print(f"não foi possível analisar o valor {valor}.")


    @analisar.register
    def _(self, valor: int):
        print(f"valor inserido é um inteiro.")


    @analisar.register
    def _(self, valor: float):
        print(f"valor inserido é um número com ponto flutuante (real).")
        
        

    @analisar.register
    def _(self, valor: str):
        print(f"valor inserido é uma string.")


    @analisar.register
    def _(self, valor: tuple|list|dict):
        print(f"valor inserido é uma coleção de dados.")
