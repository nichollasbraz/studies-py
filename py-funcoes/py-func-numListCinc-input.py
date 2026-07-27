numList = []

def numListCinc():
    while True:
        num = int(input("informe-me um número\n> "))

        if num not in numList:    
            numList.append(num)
            numList.sort(reverse=True)

            while True:
                chave = int(input(f"'{num}' adicionado\n[1] continuar\n[2] sair\n> "))
                if chave == 1:
                    break
                elif chave == 2:
                    print(
                        f"números inseridos: {len(numList)}\n"
                        f"números em ordem decrescente: {numList}"
                        )
                    if 5 in numList:
                        print("'5' faz parte da lista")
                    else:
                        print("'5' não faz parte da lista")
                    return
                else:
                    print("entrada inválida")

        else:
            print("os valores não podem ser repetidos")
            continue

numListCinc()
