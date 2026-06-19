def easyCrypto(entrada):
    print("Mensagem criptografada:")

    for letra in entrada:
        if not letra.isalpha():
            print("{}".format(letra),end="")
            continue
   
        elif ord(letra) % 2 == 0:
            print("{}".format(chr(ord(letra) - 1)),end="")
        else:
            print("{}".format(chr(ord(letra) + 1)),end="")

entrada = input("Digite um nome:\n> ")
easyCrypto(entrada)
