from math import hypot

co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))
hypo = hypot(co, ca)

print("\nValor da hipotenusa: {:.2f}".format(hypo))