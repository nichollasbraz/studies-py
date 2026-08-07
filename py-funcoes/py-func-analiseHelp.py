from time import sleep

def analise(inicio, final, passo):
    """
    A função "analise()" fará uma contagem com os parâmetros recebidos.
    
    Parâmetro "inicio": início da contagem
    Parâmetro "final": final da contagem
    Parâmetro "passo": passo da contagem
    Retorno: não possui.
    """

    if inicio < final:
        cont = inicio
        print(f"contagem de {inicio} a {final} de {passo} em {passo}:",end=" ")
        while cont <= final:
            print(f"{cont}",end=" ", flush="True")
            sleep(0.5)
            cont += passo
        print()
    else:
        cont = inicio
        print(f"contagem de {inicio} a {final} de {passo} em {passo}:",end=" ")
        while cont >= final:
            print(f"{cont}",end=" ", flush=True)
            sleep(0.5)
            cont -= passo
        print()

    sleep(0.5)

help(analise)
analise(1, 10, 2)
analise(50, 0, 2)
