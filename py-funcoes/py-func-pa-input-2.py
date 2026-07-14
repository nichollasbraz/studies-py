import os

def limparTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def PA():
    limparTerminal()
    primeiroPA = int(input("primeiro termo da PA:\n> "))
    limparTerminal()
    razaoPA = int(input("razão da PA:\n> "))
    termoPA = primeiroPA
    contador = 1
    totalPA = 0
    maisPA = 10

    while maisPA != 0:
        totalPA = totalPA + maisPA
        
        while contador <= totalPA:
            limparTerminal()
            print(f"{termoPA}", end="")
            print(" ➝  " if contador < totalPA else "", end="")
            termoPA += razaoPA
            contador += 1
        maisPA = int(input(
            "\ndeseja digitar novos termos?\n"
            "[0] sair\n"
            "> "
            ))
    
    limparTerminal()   
    print(f"foram mostrados {totalPA} termos. fechando programa...")

PA()    
