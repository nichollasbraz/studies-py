import os

def limparTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def contatos():
    contatosLista = []
    contatosHomem = 0
    contatosMulher = 0
    contatosPessMaior = 0
    
    while True:
        try:
            limparTerminal()
            contatosIdade = int(input("idade da pessoa:\n> "))

        except ValueError:
            input("entrada inválida. ENTER para continuar...")
            continue
        
        while True:
            limparTerminal()
            contatosSexo = input("sexo [M/F]:\n> ").upper()
            if contatosSexo != 'M' and contatosSexo != 'F':
                input("entrada inválida. ENTER para continuar...")
                continue    
            else:
                contatosPessoa = {
                    "idade": contatosIdade,
                    "sexo": contatosSexo
                }

                contatosLista.append(contatosPessoa)

                if contatosIdade >= 18:
                    contatosPessMaior += 1
                if contatosSexo == 'M':
                    contatosHomem += 1
                if contatosSexo == 'M' and contatosIdade < 20:
                    contatosMulher += 1

            limparTerminal()
            entrada = input(
                "pessoa cadastrada.\n"
                "deseja continuar? [S/N]:\n> "
                ).upper()
            if entrada == 'S':
                break
            else:
                limparTerminal()
                print(
                    "fechando programa...\n"
                    f"total de mulheres menores de 20 anos: {contatosMulher}\n"
                    f"total de maiores de 18 anos: {contatosPessMaior}\n"         
                    f"total de homens: {contatosHomem}"    
                    )
                return
                
contatos()
