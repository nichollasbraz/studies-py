lista = eval(input("Insira uma lista de nomes (em []): "))

for nome in lista:
    if not " " in nome and "-" not in nome:
        print(nome)
    else:
        print("Não são permitidos nomes compostos.")