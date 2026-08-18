# Declaração de Classe

class Gafanhoto():
    def __init__(self): # Método Construtor
        # Atributos de Instância
        self.nome = ""
        self.idade = 0

    # Métodos de Instância

    def aniversário(self):
        self.idade += 1
        return f"{self.nome} fez aniversário! Hoje ele(a) tem {self.idade} anos de idade."
        
    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

# Declaração de Objetos

g1 = Gafanhoto()
g1.nome = "Thalys"
g1.idade = 17

print(g1.mensagem())
print(g1.aniversário())
