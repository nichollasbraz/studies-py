def pixels(imagem):
    contador = 0

    for linha in imagem:
        for pixel in linha:
            if pixel > 0:
                contador += 1
        
    return contador

imagem = []
linhas = int(input("Quantas linhas a imagem possui? "))

for i in range(linhas):
    linha = input("Digite os valores da linha {}: ".format(i + 1))
    linha = linha.replace(",", "")
    linha = linha.split()
    linha = [int(x) for x in linha]
    imagem.append(linha)

print("\nAnalisando sua imagem...")
print(imagem)
print("Pixels não pretos: {}".format(pixels(imagem)))
