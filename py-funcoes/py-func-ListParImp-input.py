import os

def cleanTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def ListParImp():
    ListFull = []
    ListPar = []
    ListImp = []
    msg = ''

    while True:
        cleanTerminal()
        num = int(input(
            f"{msg}"
            "informe-me um número\n"
            "> "
            ))

        if num not in ListFull:
            if num % 2 == 0:
                ListPar.append(num)
                ListFull.append(num)
            else:
                ListImp.append(num)
                ListFull.append(num)
            msg = ''
        else:
            msg = "número não pode ser uma duplicata\n"
            continue

        if num <= 0:
            msg = "número não pode ser zero ou negativo\n"
            continue
        
        while True:
            cleanTerminal()
            print(
                f"{msg}"
                f"número inserido: {num}"
                )
            
            chave = int(input(
                "[1] continuar\n"
                "[2] sair\n"
                "> "
                ))

            if chave == 1:
                msg = ''
                break
            if chave == 2:
                cleanTerminal()
                print(f"lista completa: {ListFull}")

                if ListPar == []:
                    print("lista de pares: não possui")
                else:
                    print(f"lista de pares: {ListPar}")

                if ListImp == []:
                    print("lista de ímpares: não possui")
                else:
                    print(f"lista de ímpares: {ListImp}")
                return   
            else:
                msg = "entrada inválida\n"  
                continue      
                             
ListParImp()
