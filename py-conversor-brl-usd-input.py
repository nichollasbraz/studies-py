valor = float(input("Insira o valor em BRL a ser convertido em USD: "))
convert = valor / 5.03

print("\nTaxa cambial comercial do dólar: 1 USD = 5.03 BRL")
print("Valor convertido: ${:.2f}".format(convert))
