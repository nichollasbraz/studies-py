def analise(inicio, final, passo):
    """
    A função analise() fará uma contagem com os parâmetros recebidos.
    Parâmetro "inicio": início da contagem
    Parâmetro "final": final da contagem
    Parâmetro "passo": passo da contagem
    Retorno: não possui.
    """

    cont = inicio
    if inicio < final:
        while cont <= final:
            print(f"{cont}",end=" ")
            cont += passo
    else:
        while cont >= final:
            print(f"{cont}",end=" ")
            cont -= passo
    

help(analise)
