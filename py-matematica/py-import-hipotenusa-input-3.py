co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))
hypot = (co ** 2 + ca ** 2) ** (1/2)

print("\nValor da hipotenusa: {:.2f}".format(hypot))