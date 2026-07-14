pesoMaior = 0
pesoMenor = 0

for i in range(1, 7):
    peso = float(input(f"Digite o peso da {i}ª pessoa:\n> "))

    if i == 1:
        pesoMaior = peso
        pesoMenor = peso
    else:
        if peso > pesoMaior:
            pesoMaior = peso
        if peso < pesoMenor:
            pesoMenor = peso

print(
    f"Maior peso lido: {pesoMaior:.1f}kg.\n"
    f"Menor peso lido: {pesoMenor:.1f}kg."
    )
