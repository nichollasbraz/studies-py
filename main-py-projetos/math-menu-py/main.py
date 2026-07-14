import os

def limparTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    while True:
        msg = ""
        
        try:
            limparTerminal()
            numUm = int(input("digite o 1º número:\n> "))
            numDois = int(input("digite o 2º número:\n> "))
            msg = f"números: {numUm} & {numDois}\n"
        except ValueError:
            input("Entrada inválida. ENTER para continuar...")
            continue
            
        while True:
            try:                 
                limparTerminal()
                chave = int(input(
                    f"{msg}"
                    "[1] soma\n"
                    "[2] subtração\n"
                    "[3] divisão\n"
                    "[4] novos números\n"
                    "[5] sair\n"
                    "> "
                ))
            except ValueError:
                input("entrada inválida. ENTER para continuar...")
                continue

            if chave == 1:
                numSum = numUm + numDois
                msg = f"{numUm} + {numDois}: {numSum}\n"    
            elif chave == 2:
                numSub = numUm - numDois
                msg = f"{numUm} - {numDois}: {numSub}\n"  
            elif chave == 3:
                numDiv = numUm / numDois
                msg = f"{numUm} / {numDois}: {numDiv:.2f}\n"          
            elif chave == 4:
                input("redirecionando você. ENTER para continuar...")
                
                if chave == 4:
                    while True:           
                        try:
                            limparTerminal()
                            opcao = int(input(
                                "[1] alterar os dois números\n"
                                "[2] alterar apenas o primeiro\n"
                                "[3] alterar apenas o segundo\n"
                                "> "
                            ))                 
                        except ValueError:
                            input("entrada inválida. ENTER para continuar...")
                            continue

                        if opcao == 1:
                            limparTerminal()
                            numUm = int(input("novo 1º número: "))
                            msg = f"números: {numUm} & {numDois}\n"
                            limparTerminal()
                            numDois = int(input("novo 2º número: "))
                            break
                        elif opcao == 2:
                            limparTerminal()
                            numUm = int(input("novo 1º número: "))
                            msg = f"números: {numUm} & {numDois}\n"
                            break
                        elif opcao == 3:
                            limparTerminal()
                            numDois = int(input("novo 2º número: "))
                            msg = f"números: {numUm} & {numDois}\n"
                            break
                        else:
                            input("entrada inválida. ENTER para continuar...")
                
            elif chave == 5:
                limparTerminal()
                print("fechando programa...")
                return       
            else:
                input("entrada inválida. ENTER para continuar...")

menu()