import os

def cleanTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def LisCosParImp():
    num = [[],[]]
    msg = ''

    for c in range(0, 7):
        cleanTerminal()
        numTemp = int(input(
            f'{msg}'
            f'informe-me o {c + 1}º número:\n> '
            ))

        if numTemp % 2 == 0:
            num[0].append(numTemp)
            msg = f'último número: {numTemp}\n'
        else:
            num[1].append(numTemp)
            msg = f'último número: {numTemp}\n'

    num[0].sort()
    num[1].sort()
    cleanTerminal()
    print(
        f'números pares: {num[0]}\n'
        f'números ímpares: {num[1]}'
        )

LisCosParImp()
        