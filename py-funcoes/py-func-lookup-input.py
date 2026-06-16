def menu():
    while True:
        print("1) consultar contatos\n2) sair")
        
        try:
            key = int(input("> "))
        except ValueError:
            print("Utilize apenas números.")
            continue
            
        if key == 1:
            nome = input("Digite um nome:\n> ")
            sobrenome = input("Digite um sobrenome:\n> ")

            lU = lookup(nome, sobrenome)
                
        elif key == 2:
            print("Encerrando programa...")
            break

        else:
            print("Escolha um número de 1 a 2.")

def lookup(nome, sobrenome):
    contato = nome, sobrenome

    agenda = {("Elmo","Kennedy"):"(281)-330-8004",
            ("Christopher","Travis"):"(666)-454-6969",
            ("Xavier","Beard"):"(313)-444-2013",
            ("Markese","Money"):"(275)-616-1616"}
        
    if contato in agenda:
        print("{} {}".format(nome, sobrenome))
        print("{}".format(agenda[contato]))
            
    else:
        print("Contato não encontrado.")

menu_p = menu()