import random

def dadosDic():
    dados = {
             2: 1/36, 
             3: 2/36,
             4: 3/36,
             5: 4/36,
             6: 5/36,
             7: 6/36,
             8: 5/36,
             9: 4/36,
             10: 3/36,
             11: 2/36,
             12: 1/36,
             }
    
    return dados  

def somaDados(repeticoes):

    contador = {}
        
    for _ in range(repeticoes):
        dadoUm = random.randint(1,6)
        dadoDois = random.randint(1,6)

        soma = dadoUm + dadoDois
        
        if soma in contador:
            contador[soma] += 1

        else:
            contador[soma] = 1

    probTeorica = dadosDic()

    for soma in sorted(contador):
        probFreq = contador[soma] / repeticoes

        print("Soma:",soma)
        print("Ocorrências:",contador[soma])
        print("Observada: {:.5f}".format(probFreq))
        print("Teórica: {:.5f}".format(probTeorica[soma]))
        
repeticoes = 20
somaDados(repeticoes)
