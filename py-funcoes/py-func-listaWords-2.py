listaWords = ['hello',
            'mother',
            'mother',
            'love you',
            'love you',
            'wow',
            'sauce',
            'Thalys']

def removerDuplicatas(listaWords):
    return sorted(set(listaWords))

print(removerDuplicatas(listaWords))
