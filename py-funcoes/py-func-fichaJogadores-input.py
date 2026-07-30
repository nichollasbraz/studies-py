import os
from time import sleep

def ascii():
    print(r"""        _           _          _          _          _
       |.|         |.|        |.|        |.|        |.|
       ]^[         ]^[        ]^[        ]^[        ]^[
     /~`-'~\     /~`-'~\    /;`-';\    /~`-'~\    /~`-'~\
    {<|%  |>}   {<|%  |>}  {;|;;;|;}  {<|%  |>}  {<|%  |>}
     \|___|/     \|___|/    \|;;;|/    \|___|/    \|___|/
     /\    \      /   \      /   \      /   \      /   \
     |/>/|__\    /__|__\    /__|__\    /__|__\    /__|__\
    _|)   \ |    | / \ |    | / \ |    | / \ |    | / \ |
   (_,|    \)    (/   \)    (/   \)    (/   \)    (/   \)
   / \     (|_  _|)   (|_  _|)   (|_  _|)   (|_  _|)   (|_
   \_/     |,_)(_,|   |,_)(_,|   |,_)(_,|   |,_)(_,|   |,_)
""")


def cleanTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def lerNome():
    erro = ""

    while True:
        cleanTerminal()
        ascii()

        nome = input(
            f"{erro}"
            "nome do jogador:\n"
            "> "
        ).strip()

        if nome:
            return nome.upper()

        erro = "entrada inválida. tente novamente.\n"


def lerPartidas(nome):
    erro = ""

    while True:
        cleanTerminal()
        ascii()

        try:
            partidas = int(input(
                f"{erro}"
                f"> {nome}\n"
                "quantidade de partidas:\n"
                "> "
            ))

            if partidas > 99:
                erro = "quantidade máxima é de 99 partidas.\n"
                continue

            if partidas >= 0:
                return partidas

            erro = "quantidade não pode ser negativa.\n"

        except ValueError:
            pass

        erro = "entrada inválida. tente novamente.\n"


def lerGols(nome, partida):
    erro = ""

    while True:
        cleanTerminal()
        ascii()

        try:
            gols = int(input(
                f"{erro}"
                f"> {nome}\n"
                f"gols na {partida}ª partida:\n"
                "> "
            ))

            if gols >= 0:
                return gols

        except ValueError:
            pass

        erro = "entrada inválida. tente novamente.\n"


def linha(campo, valor):
    print(f"│ {campo} {'.' * (56 - len(campo) - len(str(valor)))} {valor} │")


def mostrarTabela(jogadores):
    cleanTerminal()
    ascii()

    print("┌────────────────────────────────────────────────────────────┐")
    print(f"│{'* * *     LEVANTAMENTO DOS JOGADORES     * * *':^60}│")
    print("├────┬────────────────────────┬────────────┬─────────────────┤")
    print("│ Nº │ JOGADOR                │  PARTIDAS  │  TOTAL DE GOLS  │")
    print("├────┼────────────────────────┼────────────┼─────────────────┤")

    for i, jogador in enumerate(jogadores):
        print(
            f"│ {i:<2} │ "
            f"{jogador['nome']:<22} │ "
            f"{len(jogador['gols']):^10} │ "
            f"{jogador['total']:^15} │ "
        )

    print("└────┴────────────────────────┴────────────┴─────────────────┘")


def mostrarFicha(jogador):
    cleanTerminal()
    ascii()

    print("┌────────────────────────────────────────────────────────────┐")
    print(f"│{'* * *      ESTATÍSTICAS DO JOGADOR      * * *':^60}│")
    print("├────────────────────────────────────────────────────────────┤")

    linha("NOME", jogador["nome"])
    linha("PARTIDAS", len(jogador["gols"]))
    linha("TOTAL DE GOLS", jogador["total"])

    print("├────────────────────────────────────────────────────────────┤")

    if len(jogador["gols"]) == 0:
        print("│ o jogador não disputou nenhuma partida.                    │")

    else:
        for i, gols in enumerate(jogador["gols"], start=1):

            if gols == 0:
                texto = f"na {i}ª partida não fez gols."

            elif gols == 1:
                texto = f"na {i}ª partida fez 1 gol."

            else:
                texto = f"na {i}ª partida fez {gols} gols."

            print(f"│ {texto:<59}│")

    print("└────────────────────────────────────────────────────────────┘")

def Jogadores():
    jogadores = []

    while True:

        nome = lerNome()
        partidas = lerPartidas(nome)

        gols = []

        for i in range(1, partidas + 1):
            gols.append(lerGols(nome, i))

        jogadores.append({
            "nome": nome,
            "gols": gols,
            "total": sum(gols)
        })

        cleanTerminal()
        ascii()

        msg = ""

        while True:

            opcao = input(
                f"{msg}"
                "jogador cadastrado com sucesso.\n"
                "deseja cadastrar outro? [S/N]\n"
                "> "
            ).strip().lower()

            if opcao in ("s", "n"):
                break

            msg = "entrada inválida.\n"
            cleanTerminal()
            ascii()

        if opcao == "n":
            break

    msg = ""

    while True:

        mostrarTabela(jogadores)

        try:
            indice = int(input(
                f"\n{msg}"
                "[nº] mostrar estatísticas\n"
                "[-1] novo jogador\n"
                "[-2] encerrar\n"
                "> "
            ))

        except ValueError:
            msg = "entrada inválida.\n"
            continue

        if indice == -1:
            return

        if indice == -2:
            cleanTerminal()
            ascii()
            print("\nfinalizando programa...")
            sleep(1.5)
            cleanTerminal()
            break

        if 0 <= indice < len(jogadores):
            mostrarFicha(jogadores[indice])
            input("\naperte ENTER para voltar ao levantamento...")
            msg = ""

        else:
            msg = "jogador inexistente.\n"

def cadastrarJogador(jogadores):

    nome = lerNome()
    partidas = lerPartidas(nome)

    gols = []

    for i in range(1, partidas + 1):
        gols.append(lerGols(nome, i))

    jogadores.append({
        "nome": nome,
        "gols": gols,
        "total": sum(gols)
    })

    cleanTerminal()
    ascii()

    print("jogador cadastrado com sucesso.")
    sleep(1)


def Jogadores():
    jogadores = []
    msg = ""

    while True:
        if len(jogadores) == 0:
            cadastrarJogador(jogadores)

        mostrarTabela(jogadores)

        try:
            indice = int(input(
                f"\n{msg}"
                "[nº] mostrar estatísticas\n"
                "[-1] novo jogador\n"
                "[-2] excluir jogador\n"
                "[-3] encerrar\n"
                "> "
            ))

        except ValueError:
            msg = "entrada inválida.\n"
            continue

        if indice == -1:
            cadastrarJogador(jogadores)
            msg = ""
            continue
        elif indice == -2:
            try:
                excluir = int(input(
                    "\ninforme o número do jogador que deseja excluir:\n"
                    "> "
                ))
            except ValueError:
                msg = "entrada inválida.\n"
                continue
            if 0 <= excluir < len(jogadores):
                nome = jogadores[excluir]["nome"]

                jogadores.pop(excluir)

                cleanTerminal()
                ascii()

                print(f"{nome} removido com sucesso.")
                sleep(1.5)
        elif indice == -3:
            cleanTerminal()
            ascii()

            print("\nfinalizando programa...")
            sleep(1.5)

            cleanTerminal()
            break
        elif 0 <= indice < len(jogadores):
            mostrarFicha(jogadores[indice])

            input("\naperte ENTER para voltar ao levantamento...")
            msg = ""
        else:
            msg = "jogador inexistente.\n"

Jogadores()
