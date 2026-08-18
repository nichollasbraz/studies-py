class ContaBancaria():
    """
    Em síntese, tem a funcionalidade de criar contas bancárias e permite fazer saques e depósitos.
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo

    def __str__(self):
        return f"titular : {self.titular}\nconta : {self.id}\nsaldo : r${self.saldo:,.2f}"

    def saque(self, valor):
        if valor > self.saldo:
            return f"saque negado de r${valor:,.2f}. fundos insuficientes"
        else:
            self.saldoSaque = self.saldo - valor
            return f"saldo anterior : r${self.saldo:,.2f}\nsaldo atual : r${self.saldoSaque:,.2f}(-r${valor:,.2f})"
        
    def deposito(self, valor):
        self.saldoDeposito = self.saldo + valor
        return f"saldo anterior : r${self.saldo:,.2f}\nsaldo atual : r${self.saldoDeposito:,.2f}(+r${valor:,.2f})"


c1 = ContaBancaria(112, "Gustavo Guanabara", 3000)
print(c1.saque(4000))
print(c1.deposito(700))
print(c1)
