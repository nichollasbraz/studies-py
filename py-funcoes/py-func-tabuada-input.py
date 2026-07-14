import os

def limparTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():  
    msg1 = "digite um número"
    while True:
        limparTerminal()
        num = int(input(
            f"{msg1}\n"
            f"[-1] sair\n"
            f"> "
            ))
        
        if num > 0:
            limparTerminal()
            print(f"tabuada de {num}:")
            for i in range(1, 11):
                print(f"{num} x {i:2} = {num * i}")          
            input("pressione ENTER para continuar...")

        else:
            
            print("fechando programa...")
            break

menu()