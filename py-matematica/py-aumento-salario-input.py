main_name = []

num_name = int(input("Quantos nomes serão adicionados? "))
for i in range(num_name):
    sin_name = input("Adicione um nome: ")
    main_name.append(sin_name)

main_name.sort()

print("\nLista em ordem lexicográfica (alfabética):")

for sin_name in main_name:
    print(sin_name)
