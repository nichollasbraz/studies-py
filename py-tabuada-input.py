valor = float(input("Insira o valor em R$ a ser convertido em USD: "))
convert = valor * 5.03

print("\nCotação atual (1 USD = 5,03 R$)")
print("Valor convertido: ${:.1f}".format(convert))
