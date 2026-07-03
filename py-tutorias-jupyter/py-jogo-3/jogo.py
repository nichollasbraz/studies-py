# jogo.py
import random

class JogoAdivinhacao:
    def __init__(self, minimo=1, maximo=100):
        self.minimo = minimo
        self.maximo = maximo
        self.numero_secreto = random.randint(minimo, maximo)
        self.tentativas = 0
        self.acertou = False

    def registra_palpite(self, palpite):
        self.tentativas = self.tentativas + 1

        if palpite < self.numero_secreto:
            return 'maior'
        elif palpite > self.numero_secreto:
            return 'menor'
        else:
            self.acertou = True
            return 'acertou'