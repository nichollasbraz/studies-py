nota_1 = float(input("Digite a primeira nota de Bob: "))
nota_2 = float(input("Digite a segunda nota de Bob: "))
nota_3 = float(input("Digite a terceira nota de Bob: "))
media = (nota_1 + nota_2 + nota_3) / 3

print("\nNota final: {:.1f}".format(media))
if (media == 7 or media > 7):
    print("Bob está aprovado!")
else:
    print("Bob está reprovado!")
