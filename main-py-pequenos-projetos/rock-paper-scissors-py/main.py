import random

def menu():
    print("Olá!")
    
    while True:    
        try:
            print("1) jogar\n2) sair")
            key = int(input("> "))

        except ValueError:
            print("Utilize apenas números.")
            continue

        if key == 1:
            game()

        elif key == 2:
            print("Fechando programa...")
            break
        
        else:
            print("Digite o número 1 ou 2.")
            continue

def game():
    print("Escolha entre as opções abaixo:")      
    
    while True:     
        entradaRand = random.randint(1, 3)
        
        try:    
            entrada = int(input("1) pedra\n2) papel\n3) tesoura\n> "))

        except ValueError:
            print("Utilize apenas números.")
            continue
        
        if entrada < 1 or entrada > 3:
            print("Digite um número de 1 a 3.")
            continue

        if entradaRand == 1 and entrada == 1:
            print("Empate! Ambos escolheram pedra.")
            continue
            
        elif entradaRand == 3 and entrada == 1:
            print("Você escolheu: pedra. rA9 escolheu: tesoura")
            print("Ganhou! Voltando ao menu...")
            break

        elif entradaRand == 1 and entrada == 3:
            print("Você escolheu: tesoura. rA9 escolheu: pedra")
            print("Perdeu! Voltando ao menu...")
            break

        elif entradaRand == 1 and entrada == 2:
            print("Você escolheu: papel. rA9 escolheu: pedra")
            print("Ganhou! Voltando ao menu...")
            break
        
        elif entradaRand == 2 and entrada == 1:
            print("Você escolheu: pedra. rA9 escolheu: papel")
            print("Perdeu! Voltando ao menu...")
            break

        elif entradaRand == 2 and entrada == 2:
            print("Empate! Ambos escolheram papel.")
            continue

        elif entradaRand == 2 and entrada == 3:
            print("Você escolheu: tesoura. rA9 escolheu: papel")
            print("Ganhou! Voltando ao menu...")
            break

        elif entradaRand == 3 and entrada == 2:
            print("Você escolheu: papel. rA9 escolheu: tesoura")
            print("Perdeu! Voltando ao menu...")
            break

        elif entradaRand == 3 and entrada == 3:
            print("Empate! Ambos escolheram tesoura.")
            continue

        else:
            print("Digite um número de 1 a 3.")
            continue

menu()