primeiro = int(input("Insira o primeiro termo de uma PA:\n> "))
razao = int(input("Insira a razão dessa PA:\n> "))
decimo = primeiro + (10 - 1) * razao

for c in range(primeiro, decimo + razao, razao):
    if c == decimo:
        print(f"{c}")
    else:
        print(f"{c}", end=" → ")
