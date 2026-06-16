import random

def menu():
    print("Olá!")
    while True:
        print("1) começar\n2) sair")
        try:
            key = int(input("> "))
        except ValueError:
            print("Utilize apenas números.")
            continue
        
        if key == 1:
                while True:
                    try:
                        numL = int(input("Digite o número de linhas:\n> "))
                        if numL > 0:
                            break
                        
                        print("Não pode ser um número menor ou igual a 0.")
                    except ValueError:
                        print("Utilize apenas números.")
                        continue
                
                while True:
                    try:
                        numC = int(input("Digite o número de colunas:\n> "))
                        if numC > 0:
                                break

                        print("Não pode ser um número menor ou igual a 0.")
                    
                    except ValueError:
                        print("Utilize apenas números.")
                        continue
                
                game(numL, numC) 
                
              
        elif key == 2:
            print("Fechando programa...")
            break
        
        else:
            print("Escolha um número de 1 a 2.")

def game(numL, numC):
    bombL = random.randint(0, numL - 1)
    bombC = random.randint(0, numC - 1)
    print("Linhas [0 a {}]".format(numL))
    print("Colunas [0 a {}]".format(numC))

    while True:
        try: 
            tentativaL = int(input("Qual a linha?\n> "))
            if tentativaL < 0 or tentativaL >= numL:
                print("Linha inválida. Tente de novo.")
                continue
        
        except ValueError:
            print("Utilize apenas números.")
            continue 
      
        while True:
            try:
                tentativaC = int(input("Qual a coluna?\n> "))
                if 0 <= tentativaC < numC:
                        break

                print("Coluna inválida.")
                
            except ValueError:
                print("Utilize apenas números.")
                continue

        if tentativaL == bombL and tentativaC == bombC:
            print("Bomba encontrada! Voltando ao menu...")
            break 
    
        else:
            print("Posição errada. Tente de novo.")

menuP = menu()