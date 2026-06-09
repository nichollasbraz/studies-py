frase = input("Digite uma frase: ")

conteudo = frase.split()
resultado = []

for palavra in conteudo:
    if len(palavra) == 5:
        resultado.append("&&&&&")
    else:
        resultado.append(palavra)

print(" ".join(resultado))
