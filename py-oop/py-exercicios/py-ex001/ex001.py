# Declaração de Classe

class Gafanhoto():
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
        
    def mensagem(self):
        if self.nome == "%null%" and self.idade == 0:
            return f"Não foram inseridos valores na classe."
        else:
            return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

# Declaração de Objetos

g1 = Gafanhoto("Thalys", 17)

print(g1.mensagem())
print(g1.aniversário())

g2 = Gafanhoto()

print(g2.aniversário())
print(g2.mensagem())
