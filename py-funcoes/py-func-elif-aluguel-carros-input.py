def aluguel_carros(dias, kms):
    aluguel_diario = (dias * 39.99) + (kms * 0.15)
    aluguel_desconto_1 = aluguel_diario * 0.15
    aluguel_desconto_2 = aluguel_diario * 0.05

    if dias >= 30:
        total_aluguel = aluguel_diario - aluguel_desconto_1
        print("\nMontante: R${:.2f}".format(aluguel_diario))
        print("Desconto de 15%(-R${:.2f}): R${:.2f}".format(aluguel_desconto_1, total_aluguel))
    
    elif dias >= 7:
        total_aluguel = aluguel_diario - aluguel_desconto_2
        print("\nMontante: R${:.2f}".format(aluguel_diario))
        print("Desconto de 5%(-R${:.2f}): R${:.2f}".format(aluguel_desconto_2, total_aluguel))
    
    else:
        total_aluguel = aluguel_diario
        print("\nMontante: R${:.2f}".format(total_aluguel))

dias = int(input("Insira a quantidade de dias que o automóvel foi alugado: "))
kms = float(input("Insira a quilometragem rodada: "))

aluguel_carros(dias, kms)
