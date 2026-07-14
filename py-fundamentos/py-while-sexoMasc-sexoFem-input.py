sexoMasc = 0
sexoFem = 0

while True:
    sexo = input(
    "[M/F] 'M' para masculino e 'F' para feminino\n[0] sair\n> "
    ).upper()
    
    if sexo == 'M':
        sexoMasc += 1
        continue

    elif sexo == 'F':
        sexoFem += 1
        continue

    elif sexo == '0':
        print(
        f"Foram lidas {sexoMasc} pessoas do sexo masculino.\n"
        f"Foram lidas {sexoFem} pessoas do sexo feminino."
        )
        break

    else:
        print("Entrada inválida. Tente de novo")
        continue
    