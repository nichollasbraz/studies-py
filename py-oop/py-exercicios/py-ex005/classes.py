class ContaBancaria():
    """
    Em síntese, tem a funcionalidade de criar contas bancárias e permite fazer saques e depósitos.
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self._titular = nome
        self.__saldo = saldo

    def __str__(self):
        # return f"titular : {self.titular}\nconta : {self.id}\nsaldo : r${self.saldo:,.2f}"
        return f"dados da conta: {self.__dict__}"

    def saque(self, valor):
        valor = abs(valor)
        if valor > self.__saldo:
            return f"saque negado de r${valor:,.2f}. fundos insuficientes"
        else:
            saldo_anterior = self.__saldo
            self.__saldo -= valor
            return f"saldo anterior : r${saldo_anterior:,.2f}\nsaldo atual : r${self.__saldo:,.2f}(-r${valor:,.2f})"
        
    def deposito(self, valor):
        valor = abs(valor)
        saldo_anterior = self.__saldo
        self.__saldo += valor
        return f"saldo anterior : r${saldo_anterior:,.2f}\nsaldo atual : r${self.__saldo:,.2f}(+r${valor:,.2f})"


