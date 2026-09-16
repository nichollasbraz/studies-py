arquivoRanking = "ranking.txt"

def salvarPontuacao(nome, jogadas):

    nome = nome.strip()[:15]

    with open(arquivoRanking, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome};{jogadas}\n")

def carregarRanking():
    ranking = []

    try:
        with open(arquivoRanking, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()

                if linha == "":
                    continue

                partes = linha.split(";")

                if len(partes) != 2:
                    continue

                nome, jogadas = partes

                try:
                    ranking.append((nome, int(jogadas)))
                except ValueError:
                    continue

    except FileNotFoundError:
        pass

    ranking.sort(key=lambda jogador: jogador[1])

    return ranking

def mostrarRanking():
    ranking = carregarRanking()

    print("┌────────────────────────────────────────┐")
    print("│ *  *  *        RANKING        *  *  *  │")
    print("├────────────────────────────────────────┤")

    if len(ranking) == 0:
        print("│ Nenhuma pontuação registrada.          │")
    else:
        ranking = ranking[:10]
        
        for posicao, (nome, jogadas) in enumerate(ranking, start=1):
            texto = f"{posicao}. {nome[:15]}"
            largura_util = 36
            pontinhos = "." * max(
                1,
                largura_util - len(texto) - len(str(jogadas))
            )
            print(
                f"│ {texto} {pontinhos} {jogadas} │"
            )
           
    print("└────────────────────────────────────────┘")