from rich import print
from rich.table import Table

tabela = Table(title="TABELA DE PREÇOS (TESTE):")

tabela.add_column("PRODUTO", justify="center")
tabela.add_column("PREÇO (R$)", justify="center")

tabela.add_row("Lapiseira","R$2,70")
tabela.add_row("Caneta azul","R$1,50")

print(tabela)
