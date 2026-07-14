from datetime import date

data = date.today().year
idadeMaior = 0
idadeMenor = 0

for i in range(1, 8):
    idadePessoa = int(input(f"Digite o ano em que {i}ª pessoa nasceu:\n> "))
    idadeMin = data - idadePessoa

    if idadeMin >= 18:
        idadeMaior += 1
    else:
        idadeMenor += 1
    
print(
    f"Temos {idadeMaior} pessoas maiores de idade.\n"
    f"Temos {idadeMenor} pessoas menores de idade."
    )
