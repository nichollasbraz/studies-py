def menu():
    while True:
        try:
            print("1) jogar\n2) sair")
            key = int(input("> "))
        
        except ValueError:
            print("Digite apenas números.")
            continue

        if key == 1:
            game()

        elif key == 2:
            print("Fechando programa...")
            break

        else:
            print("Digite o número 1 e 2.")
            continue

def game():
    portas = {
        1: [1,2],
        2: [1,3],
        3: [3]
    }
    
    fase = 1

    print("Escolha uma das portas:")
    while True:
        try:
            print("1) porta branca\n2) porta preta\n3) porta carmesim")
            entrada = int(input("> "))
            
        except ValueError:
            print("Digite apenas números.")
            continue

        if entrada not in portas:
            print("Digite um número de 1 a 3.")

        elif entrada in portas[fase]:   
            if fase == 3:
                print("Venceu! Voltando ao menu...")
                break
            
            print("Correto! Prosseguindo para a fase {}.".format(fase + 1))

            fase += 1
            continue

        else:
            print("Perdeu! Voltando ao menu...")
            break

menu()
