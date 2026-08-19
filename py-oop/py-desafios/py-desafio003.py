from rich import print
from rich.panel import Panel

class Churrasco:
    precoCarne = 82.40
    mediaConsumo = 0.400

    def __init__(self, titulo="sem nome", qtd="null"):
        self.titulo = titulo
        self.qtdPes = qtd

    def calc_qtd_carne(self) -> float:
        return self.qtdPes * Churrasco.mediaConsumo

    def calc_preco_total(self) -> float:
        return self.calc_qtd_carne() * self.precoCarne

    def calc_preco_individual(self) -> float:
        return self.calc_preco_total() / self.qtdPes

    def __str__(self):
        if self.qtdPes == "null":
            return f"valor não pode ser zero."
        else:
            return f"{self.titulo}\n{self.qtdPes}\n{self.calc_preco_total()}\n{self.calc_preco_individual()}\n{self.calc_qtd_carne()}"

    def tabela(self):
        cont = f"analisando [blue]{self.titulo}[/] com [blue]{self.qtdPes}[/] convidados...\n"
        cont += f"cada convidado comerá [blue]{self.mediaConsumo:.1f}kg[/], cada kg custando [blue]r${self.precoCarne:.2f}[/].\n"
        cont += f"recomendo comprar [blue]{self.calc_qtd_carne():.1f}kg[/] de carne.\n"
        cont += f"o custo total será de [blue]r${self.calc_preco_total():.2f}.[/]\n"
        cont += f"cada pessoa pagará [blue]r${self.calc_preco_individual():.2f}[/] para participar." 
        painel = Panel(cont, title=f"análise de {self.titulo}", width=60)
        print(painel)

c1 = Churrasco("churrasco com os crias", 15)
print(c1)
c1.tabela()
