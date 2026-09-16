from functools import singledispatchmethod

class Carteira():

    def __init__(self, saldo: int|float = 0):
        self.__saldo = saldo


    def __str__(self):
        return f"saldo atual: r${self.__saldo:,.2f}."


    def __eq__(self, outro: int|float = 0) -> bool:
        if self.__saldo == outro.__saldo:
            return True
        else:
            return False


    def __ne__(self, outro: int|float = 0) -> bool:
        if self.__saldo != outro.__saldo:
            return True
        else:
            return False


    def __le__(self, outro: int|float = 0) -> bool:
        if self.__saldo >= outro.__saldo:
            return True
        else:
            return False
        

    def __iadd__(self, outro: int|float = 0):
        self.__saldo += outro
        return self


    def __isub__(self, outro: int|float = 0):
        self.__saldo -= outro
        return self
    

    @property
    def saldo(self):
        return self.__saldo


    @saldo.setter
    def saldo(self, valor: int|float = 0):
        raise PermissionError("você não pode alterar o saldo desta forma.")