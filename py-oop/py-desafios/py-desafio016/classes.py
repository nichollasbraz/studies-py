from hashlib import sha256

class SHA256(): #SHA: Secure Hash Algorithm

    def __init__(self):
        self.__hash = None

    def validar(self, senha):
        __senha_user = sha256(senha.encode('UTF-8')).hexdigest()

        if self.__hash == __senha_user:
            print("senha confere!")

        else:
            raise PermissionError("senha incorreta.")
            

    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def senha(self, senha):
        if len(senha) > 0:
            self.__hash = sha256(senha.encode('UTF-8')).hexdigest()

            print("senha salva com sucesso.")
        else:
            raise ValueError("senha inválida.")

