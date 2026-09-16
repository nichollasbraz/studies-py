from hashlib import sha256

class ContaBancaria():
    """
    Em síntese, tem a funcionalidade de criar contas bancárias e permite fazer saques e depósitos.
    """
    def __init__(self, id: int, nome: str = None, saldo: float = 0, chave: str = None):
        self._id = id # protegido (#)
        self._titular = nome # protegido (#)
        self.__saldo = saldo # privado (-)
        if chave == None:
            chave = self.pede_senha()
        self.__hash = sha256(chave.encode('UTF-8')).hexdigest()
        print(
            f"conta criada com sucesso.\n"
            f"id : {id}\n"
            f"titular : {nome}\n"
            f"saldo : r${saldo:,.2f}"
            )

    def pede_senha(self) -> str:
        from pwinput import pwinput

        while True:
            senha = pwinput("senha : ").strip()
            if len(senha) >= 6:   
                break
            else:
                print("senha precisa ser maior ou igual a 6 caracteres.")
                continue

        return senha

    def validar_senha(self, chave: str) -> bool:
        usuario = sha256(chave.encode('UTF-8')).hexdigest()
        if usuario == self.__hash:
            return True
        else:
            return False

    def __str__(self):
        return f"estado atual: {self.__dict__}"

    def saque(self, valor, chave: str = None):
        if chave is None:
            chave = self.pede_senha()

        if self.validar_senha(chave):
            if valor > self.__saldo:
                print (f"saque negado de r${valor:,.2f}. fundos insuficientes")
            else:
                self.saldoSaque = self.__saldo - valor
                print(f"saldo anterior : r${self.__saldo:,.2f}\nsaldo atual : r${self.saldoSaque:,.2f}(-r${valor:,.2f})")
        else:
            print("senhas não coincidem. saque não autorizado.")

    def deposito(self, valor):
        self.saldoDeposito = self.__saldo + valor
        return f"saldo anterior : r${self.__saldo:,.2f}\nsaldo atual : r${self.saldoDeposito:,.2f}(+r${valor:,.2f})"


    @property
    def titular(self):
        return self._titular


    @titular.setter
    def titular(self, novoTitular: str = None,):
        novoTitular = self.pede_senha()

        if self.validar_senha(novoTitular):
            if len(novoTitular) < 3:
                print("nome do titular deve ser no mínimo 3 caracteres.")
            else:
                self._titular = novoTitular
        else:
            print("senhas não coincidem.")
