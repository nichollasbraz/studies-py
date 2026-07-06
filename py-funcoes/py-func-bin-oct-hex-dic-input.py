def conversor():
    num = int(input("Digite um número inteiro:\n> "))
    
    print(
        "[1] converter para binário\n"
        "[2] converter para octal\n"
        "[3] converter para hexadecimal"
          )

    conversoes = {
        1: bin,
        2: oct,
        3: hex,
    }

    key = int(input("> "))

    if key in conversoes:
        print(conversoes[key](num)[2:])
    else:
        print("Operação inválida.")
    
conversor()