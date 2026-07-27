galera = list()
galeraDado = list()
totMaior = totMenor = 0
for d in range(0,5):
    galeraDado.append(str(input("nome: ")))
    galeraDado.append(int(input("idade: ")))
    galeraDado.append(str(input("sexo: ")))
    galera.append(galeraDado[:])
    galeraDado.clear()

for pessoa in galera:
    print(f"{pessoa[0]} tem {pessoa[1]} anos e é do sexo {pessoa[2]}.", end=" ")
    if pessoa[1] >= 21:
        print(f"{pessoa[0]} é maior de idade.")
        totMaior += 1
    else:
        print(f"{pessoa[0]} é menor de idade.")
        totMenor += 1

if totMaior == 1:
    print(f"possuímos uma pessoa maior de idade.")
elif totMaior > 1:
    print(f"possuímos {totMaior} pessoas maiores de idade.")
else:
    print("não possuímos pessoas maiores de idade.")

if totMenor == 1:
    print(f"possuímos uma pessoa menor de idade.")
elif totMenor > 1:
    print(f"possuímos {totMenor} pessoas menores de idade.")
else:
    print("não possuímos pessoas menores de idade.")
