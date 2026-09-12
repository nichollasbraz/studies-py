class Diario():

    def __init__(self):

        self.__segredos = []
        self.__senha = "CeV!@"
        self.__acesso = False


    @property
    def ler(self):
        if self.__acesso:
            return self.__segredos
        else:
            raise ValueError("senha incorreta.")


    @ler.setter
    def ler(self, senha):
        if senha == self.__senha:
            self.__acesso = True
        else:
            self.__acesso = False

            raise ValueError("senha incorreta.")


    @property
    def escrever(self):
        return self.__segredos


    @escrever.setter
    def escrever(self, msg):

        self.__segredos.append(msg)

        return "segredo registrado."
