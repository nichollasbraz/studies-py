from rich import print
from rich.panel import Panel

class Produto:
    loja = "Loja do Curso em Vídeo"

    def __init__(self, item="desconhecido", valor="desconhecido"):
        self.item = item
        self.valor = valor

    def __str__(self):
        if self.item == "desconhecido" or self.valor == "desconhecido":
            return "produto não encontrado."

        return f"{self.item}\nR${self.valor:,.2f}"

    def etiqueta(self):
        conteudo = f"{self.item.center(34)}"
        conteudoPreco = f"R${self.valor:,.2f}"
        conteudo += f"{conteudoPreco.center(34, '.')}"
        painel = Panel(conteudo, title="produto", width=38)
        print(painel)

p1 = Produto("iPhone 15 256GB", 2599.99)
p2 = Produto("Bobbie Goods", 67.99)
print(p1)
p1.etiqueta()
p2.etiqueta()
    