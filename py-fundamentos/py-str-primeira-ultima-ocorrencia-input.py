nome = str(input("Digite seu nome completo: ")).strip()
nome = nome.split()

print("\nAnalisando seu nome...")
print("Primeiro nome: {}".format(nome[0]))
print("Último nome: {}".format(nome[len(nome)]))
