from random import randint
from time import sleep
import os

def cleanTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def MegaSena():
    listNum = []
    listJogos = []
    msg = ''

    while True:
        cleanTerminal()
        try:
            qtyJogos = int(input(
            f"{msg}"
            "informe-me a quantidade de jogos que serão sorteados:\n"
            "> "
            ))
        except ValueError:
            msg = 'entrada inválida. tente de novo\n'
            continue

        if qtyJogos <= 0:
            msg = 'entrada inválida. tente de novo\n'
            continue
            
        for _ in range(qtyJogos):

            while len(listNum) < 6:
                num = randint(1, 60)

                if num not in listNum:
                    listNum.append(num)

            listNum.sort()
            listJogos.append(listNum[:])
            listNum.clear()

        cleanTerminal()
        if qtyJogos > 1:
            print(f"gerando {qtyJogos} jogos...")
        else: 
            print(f"gerando {qtyJogos} jogo...")

        for i, jogo in enumerate(listJogos, start=1):
            print(f"{i:02} : ", end="")
            print(*jogo)
            sleep(1)
        listJogos.clear()

        while True:
            tecl = input("\nreiniciar? [s/n]\n> ").lower()

            if tecl == 's':
                print("reiniciando...")
                msg = ''
                sleep(1)
                break
            else:
                print("finalizando programa... boa sorte!")
                sleep(1)
                return
            
MegaSena()
