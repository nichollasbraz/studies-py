import os

def limparTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def estatisticaProdutos():
    prodLista = []
    prodSum = 0
    prodMaiorMil = 0

    while True:
        limparTerminal()
        try:
            prodNome = str(input("nome do produto:\n> ")).lower()
        except ValueError:
            input("entrada inválida. ENTER para continuar...")
            continue
        
        while True:
            limparTerminal()
            try:
                prodPreco = float(input("preço do produto:\n> r$ "))
                if prodPreco <= 0:
                    input("entrada inválida. ENTER para continuar...")
                    continue
            except ValueError:
                input("entrada inválida. ENTER para continuar...")
                continue
        
            produto = {
            'nome':prodNome,
            'preço':prodPreco 
            }

            prodLista.append(produto)

            if len(prodLista) == 1:
                prodMaior = produto
                prodMenor = produto    
            if produto['preço'] > prodMaior['preço']:
                prodMaior = produto        
            if produto['preço'] < prodMenor['preço']:
                prodMenor = produto            
            if prodPreco > 1000:
                prodMaiorMil += 1

            prodSum += prodPreco
        
            limparTerminal()
            chave = input(
                f"{produto['nome']} (r${produto['preço']:.2f}) cadastrado.\n"
                "deseja continuar? [S/N]\n> "
                ).upper()
            if chave == 'S':
                break 
            else:
                limparTerminal()
                print(
                f"total da compra: r${prodSum:.2f}\n"
                f"produtos (+r$1000.00): {prodMaiorMil}\n"
                f"produto mais barato (r${prodMenor['preço']:.2f}): {prodMenor['nome']}"
                )
                return
            
estatisticaProdutos()
