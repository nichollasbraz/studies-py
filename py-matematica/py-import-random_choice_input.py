import random

lista = eval(input("Escreva uma lista de itens (ex: ['Thalys']): "))
r_lista = random.choice(lista)

print("\nItem escolhido aleatoriamente: {}".format(r_lista))
