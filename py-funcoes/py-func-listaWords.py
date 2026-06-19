listaWords = ['hello',
            'mother',
            'mother',
            'love you',
            'Thalys',
            'wow',
            'sauce',
            'Thalys']

def removerDuplicatas(listaWords):
    contagem = {}

    for palavra in listaWords:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1

    return sorted(contagem) 

print(removerDuplicatas(listaWords))
