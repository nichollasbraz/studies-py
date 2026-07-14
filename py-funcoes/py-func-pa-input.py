def PA():
    primeiroPA = int(input("primeiro termo da PA:\n> "))
    razaoPA = int(input("razão da PA:\n> "))
    termoPA = primeiroPA
    contador = 1
    totalPA = 0
    maisPA = 10

    while maisPA != 0:
        totalPA = totalPA + maisPA
    
        while contador <= totalPA:
            print(f"{termoPA}", end="")
            print(" ➝  " if contador < totalPA else "", end="")
            termoPA += razaoPA
            contador += 1
        maisPA = int(input(
            "\ndeseja digitar novos termos?\n"
            "[0] sair\n"
            "> "
            ))
        
    print("fechando programa...")

PA()    
