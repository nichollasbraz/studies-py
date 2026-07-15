import os

def limparTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def banco():
    while True:
        limparTerminal()

        try:
            valor = int(input("valor a ser sacado:\n> "))
            if valor <= 0:
                input("entrada inválida. ENTER para continuar...")
                continue
        except ValueError:
            input("entrada inválida. ENTER para continuar...")
            continue

        total = valor
        ced = 50
        totalCed = 0

        limparTerminal()
        print(f"R${valor}:")

        while True:
            if total >= ced:
                total -= ced
                totalCed += 1

            else:
                if totalCed > 0:
                    print(f"total de {totalCed:02} cédula(s) de R${ced}")

                totalCed = 0

                if ced == 50:
                    ced = 20
                elif ced == 20:
                    ced = 10
                elif ced == 10:
                    ced = 5
                elif ced == 5:
                    ced = 1
                else:
                    break
        
        msg = ''
        while True:        
            chave = input(
                f"{msg}"
                f"deseja sacar novamente? [S/N]: "
                ).upper()

            if chave == "S":
                break
            elif chave == "N":
                limparTerminal()
                print("encerrando programa...")
                return
            else:
                msg = "digite apenas S ou N.\n"

banco()