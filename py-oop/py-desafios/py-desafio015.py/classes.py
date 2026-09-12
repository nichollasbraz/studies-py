class Diario():

    def __init__(self, senhamestra = "CeV!@"):

        self.__segredos = []
        self.__senha = senhamestra.strip()


    def escrever(self, msg):
        if isinstance(msg, str) and len(msg) > 0:
            self.__segredos.append(msg.strip())

            print("segredo registrado.")


    def ler(self, senha = None):
        if senha == self.__senha:
            if len(self.__segredos) == 0:
                print("não possuo segredos para te esconder.")
            else:
                for segredo in self.__segredos:
                    print(f'"{segredo}"')
        else:
            raise PermissionError("ninguém sabe da minha senha!")


    def nova_senha(self, novasenha, senha):
        if senha == self.__senha:
            self.__senha = novasenha
        
            print("nova senha adicionada ao diário.")
        else:
            raise PermissionError("ninguém sabe da minha senha!")

    @property
    def senha(self):
        raise PermissionError("ninguém sabe da minha senha!")
        
            


    
