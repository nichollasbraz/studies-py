from math import sqrt, pow

co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))
hipotenusa = sqrt(pow(ca, 2) + pow(co, 2))

print("\nValor da hipotenusa: {:.2f}".format(hipotenusa))