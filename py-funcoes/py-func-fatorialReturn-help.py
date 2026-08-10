def fatorial(num, show=False):
    """
    A função calcula o fatorial de um número.
    Parâmetro 'num' é o número a ser fatorado.
    Parâmetro 'show' é a opção facultativa do desenvolvimento da fatoração.
    
    A função no final retorna 'fat' ao usuário.
    """

    fat = 1
    for c in range(num, 0, -1):
        if show == True:
            print(f"{c}", end="")
            if c > 1:
                print(f" x ", end="")
            else:
                print(f" = ", end="")
            
        fat *= c
    return fat


help(fatorial)
print(fatorial(5, show=True))
