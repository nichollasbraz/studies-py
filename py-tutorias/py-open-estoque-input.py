def numChars(filename):
    file = open(filename, "r", encoding="UTF-8")
    content = file.read()
    file.close()

    print("\nConteúdo do arquivo {}:".format(filename))
    print(content)
    return len(content)

filename = input(str("Digite o nome do arquivo: "))
numChars(filename)
