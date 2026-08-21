from rich import print
from rich.panel import Panel

class Gamer():
    def __init__(self, name, username):
        self.name = name
        self.username = username
        self.jogoLst = []

    def add_favoritos(self, jogo = 0):
        if jogo == 0:
            print(f"valor não pode ser vazio!")
            pass

        elif jogo not in self.jogoLst:
            self.jogoLst.append(jogo)
        self.jogoLst = sorted(self.jogoLst, key=str.lower)

    def ficha(self):
        conteudo = f"[grey]nome real:[/] [white]{self.name}[/]\n"
        conteudo += f"[grey]jogos favoritos:[/]"

        if self.jogoLst != []:
            for _, jogo in enumerate(self.jogoLst):
                conteudo += f"\n[white]{jogo}"
        else:
            conteudo += "\nnenhum jogo adicionado."

        painel = Panel(conteudo, title=f"[white]<{self.username}>[/]", width=35)
        print(painel)

g1 = Gamer("Thalys Nogueira", "thxlys")
g1.add_favoritos()
g1.ficha()
