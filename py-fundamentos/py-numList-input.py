import os

def cleanTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def numeros():
    numList = []
    msg = ''

    while True:
        try:
            cleanTerminal()
            print(f"{msg}", end="")
            num = int(input("informe-me um número\n[-1] sair\n> "))
            if num == -1:    
                cleanTerminal()
                if numList == []:
                    print("lista sem valores adicionados")
                    break
                else:
                    print(f"lista completa: {numList}")
                    break
            if num < -1:
                msg = "números negativos não serão adicionados\n"
                continue
            if num == 0:
                msg = "número não -pode ser zero\n"
                continue
            if num not in numList:
                numList.append(num)
                msg = f"último número: {numList[-1]}\n"
            else:
                msg = "números iguais não serão adicionados\n"
                continue
        except ValueError:
            msg = "entrada inválida. tente de novo\n"
            continue
        
numeros()
        