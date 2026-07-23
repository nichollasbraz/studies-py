def porExtenso(num):
    numExtenso = (
        (1, 'um'),
        (2, 'dois'),
        (3, 'três'),
        (4, 'quatro'),
        (5, 'cinco'),
        (6, 'seis'),
        (7, 'sete'),
        (8, 'oito'),
        (9, 'nove'),
        (10, 'dez'),
    )

    print(numExtenso[num - 1][1])

while True:
    try: 
        num = int(input("digite um número de 1 a 10:\n> "))
    except ValueError:
        input("entrada inválida. ENTER para continuar...")
        continue

    if num > 10:
        input("entrada inválida. ENTER para continuar...")
        continue
    elif num < 1:
        input("entrada inválida. ENTER para continuar...")
        continue
    
    porExtenso(num)    
