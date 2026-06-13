def menu():
    erros = 0
    print("\nOlá!")

    while True:
        print("1) entrar\n2) exibir tentativas\n3) sair")
        try:
            key = int(input("> "))
        except ValueError:
            print("Digite apenas números.")
            continue
    
        if key == 1:
            erros = entrada(erros)

        elif key == 2:
            tentativas = print("Foram efetuadas {} tentativas.".format(erros))

        elif key == 3:
            print("Até breve! Fechando programa...")
            break

        else:
            print("Entrada inválida!")


def entrada(erros):
    senha_og = "pythonEhLegal"
    
    if erros >= 3:
        print("Você já atingiu o limite de tentativas. Voltando ao menu...")
        return erros
   
    senha_user = input("Digite a senha:\n> ")
   
    if senha_user == senha_og:
        print("Correto! Entrando no sistema...")
        return 0

    erros += 1


    if erros >= 3:
        print("Você atingiu o limite de tentativas. Voltando ao menu...")
    else:
        print("Senha incorreta! Voltando ao menu...")
    
    return erros
    
menu()
