import random

def menu():
    print("Olá!")

    while True:
        try:
            print("1) jogar\n2) sair")
            chave = int(input("> "))
        
        except ValueError:
            print("Insira apenas números.")
            continue

        if chave == 1:
            while True:
                try:
                    faixaNum = int(input("Digite um número de 1 a 99:\n> "))
                    if faixaNum > 0 and faixaNum <= 99:       
                        jogoNum(faixaNum)
                        break
                   
                    print("Deve ser um número entre 1 a 99.")
                
                except ValueError:
                    print("Insira apenas números.")
                    continue   

        elif chave == 2:
            print("Fechando programa...")
            break

        else:
            print("Digite o número 1 ou 2.")
            continue

def jogoNum(faixaNum):
    randNum = random.randint(1, faixaNum)   
    qntTentativas = 5

    print("Número está entre 1 e {}. Você possui 5 tentativas.".format(faixaNum))
    while True:
        try:
            userNum = int(input("Qual o número?\n> "))
           
            if userNum == randNum:
                print("Correto! Voltando ao menu...")
                return

            qntTentativas -= 1
           
            if qntTentativas == 0:
                print("Você perdeu! O número era {}. Voltando ao menu...".format(randNum))
                return
           
            if userNum < randNum:
                print("Está acima! Tentativas restantes: {}".format(qntTentativas))
                continue
        
            else:
                print("Está abaixo! Tentativas restantes: {}".format(qntTentativas))
                continue

        except ValueError:
            print("Insira apenas números.")
            continue
            
menu()