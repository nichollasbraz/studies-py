import os

def cleanTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def matrizLst():
    sumPar = sumCol = iMaior = 0
    matriz = [[0,0,0],[0,0,0],[0,0,0]]
    msg = ''

    for c in range(0,3):   
        for i in range (0,3):
            cleanTerminal()
            matriz[c][i] = int(input(
                f"{msg}"
                f"informe-me um número [{c},{i}]\n> "
                ))
            msg = f'> {matriz[c][i]}\n'

    cleanTerminal()
    for c in range(0,3):
        for i in range(0,3):
            print(f'[{matriz[c][i]:^5}]', end=" ")
            if matriz[c][i] % 2 == 0:
                sumPar += matriz[c][i]
                
        print()

    for c in range(0,3):
        sumCol += matriz[c][2]

    iMaior = max(matriz[1])

    print(
        f"\nsoma dos pares: {sumPar}\n"
        f"soma da terceira coluna: {sumCol}\n"
        f"maior número da segunda linha: {iMaior}"
        )
    
matrizLst()
