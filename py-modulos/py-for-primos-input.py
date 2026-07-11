num = int(input("Digite um número:\n> "))
cont = 0

for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")
        cont += 1
    
if cont == 2:
    print("\nÉ um número primo.")
else:
    print("\nNão é um número primo.")
    