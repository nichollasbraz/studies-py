estacao = None

def season(num):
    if 1 <= num <= 3:
        estacao = "verão"

    elif 4 <= num <= 6:
        estacao = "outono"

    elif 7 <= num <= 9:
        estacao = "inverno"
        
    elif 10 <= num <= 12:
        estacao = "primavera"
    else: 
        print("\nValor inválido!")
        return
    
    print ("\nEstação atual: {}".format(estacao))

num = int(input("Digite um número: "))
season(num)
