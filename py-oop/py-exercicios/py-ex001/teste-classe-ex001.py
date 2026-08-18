class Gafanhoto():
    """
    Essa classe cria Gafanhoto, uma pessoa que possui um nome e idade.
    
    Para criar uma nova pessoa, utilize:
    variável = Gafanhoto(nome, idade).
    """

    def __init__(self, nome = "%null%", idade = 0): # Método Construtor
        # Atributos de Instância
        self.nome = nome
        self.idade = idade

    # Métodos de Instância

    def aniversário(self):
        if self.nome == "%null%" and self.idade == 0:
            return f"Não foram inseridos valores na classe."
        else:
            self.idade += 1
            return f"{self.nome} fez aniversário! Hoje ele(a) tem {self.idade} anos de idade."

    def __str__(self):
        if self.nome == "%null%" and self.idade == 0:
            return f"Não foram inseridos valores na classse."
        else:
            return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

    def __getstate__(self):
        return f"Estados : Nome : {self.nome} ; Idade : {self.idade}"

g1 = Gafanhoto("Thalys", 26)
print(g1.aniversário())
print(g1.__dict__)
print(g1.__getstate__())
print(g1)

 # print(g1.__doc__) Dunder Attribute
