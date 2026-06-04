print("Digite o preço do produto em R$:",end="")
produto = float(input(" "))
promo = produto - (produto * 0.05)

print("\nPreço original: R${:.2f}".format(produto))
print("Preço novo (5% de desconto): R${:.2f}".format(promo))
