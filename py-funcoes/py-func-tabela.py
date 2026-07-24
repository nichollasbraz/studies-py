def tabela():
    lista = (
        'Thalys', 55.99,
        'Nogueira', 69.99,
        'UniFOA', 1059.90,
        'FGV IDT', 750,00,
        'Bunda de Tales', 0.5,
        'Bunda de Petrus', 0.05,
        'Bucholine', 13.13,
        'Bolsonaro', 22.67,
        'Lule', 13.69,
        'MC Brankim da GM', 6969.69
        )

    for i in range(0, len(lista)):
        if i % 2 == 0:
            print(f'{lista[i]:.<30}', end="")
        else:
            print(f'R${lista[i]:>7}') 

tabela()
