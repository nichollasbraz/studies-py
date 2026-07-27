import os

def cleanTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def matrizLst():
    matriz = [[],[],[]]
    msg = ''

    for c in range(0,3):   
        for i in range (0,3):
            cleanTerminal()
            matTemp = int(input(
                f"{msg}"
                f"informe-me um número [{i},{c}]\n> "
                ))
            matriz[0].append(matTemp) 

    print(matriz)

matrizLst()