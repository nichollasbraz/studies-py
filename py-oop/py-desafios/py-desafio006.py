from rich import print

class Caneta():
    cores = {
        "azul":"[blue]",
        "vermelho":"[red]",
        "vermelha":"[red]",
        "amarela":"[yellow]",
        "amarelo":"[yellow]",
        "verde":"[green]"
        }

    def __init__(self, corCaneta):
        self.cor = corCaneta.lower().strip()
        self.tampada = True

    def destampar(self):
        self.tampada = False

    def tampar(self):
        self.tampada = True

    def quebrar_linha(self, qty = 1):
        for _ in range(qty):
            print()

    def escrever(self, texto = ""):
        if not self.tampada:
            print(f"{self.cores[self.cor]}{texto}", end="")
        else:
            print(f"a {self.cores[self.cor]}caneta[/] está tampada!")


c1 = Caneta("AZUL")
c1.escrever("teste")
c2 = Caneta("amarelo")
c2.destampar()
c2.escrever("t")
c1.destampar()
c1.escrever("h")
c2.escrever("a")
c1.escrever("l")
c2.escrever("y")
c1.escrever("s")
