def buscarLinhas(filename, word):
    archive = open(filename, "r", encoding="UTF-8")
    line = archive.readlines
    archive.close
    filtered = []

    for line in lines:
        if word in line:
            filtered.append(line)
        
    return filtered


filename = input("Digite o arquivo a ser procurado: ")
word = input("Digite a palavra a ser procurada: ")

result = buscarLinhas(filename, word)
