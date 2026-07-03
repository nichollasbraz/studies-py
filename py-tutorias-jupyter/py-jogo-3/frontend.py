# frontend.py
import exibicao
from jogo import JogoAdivinhacao

def jogar():
    jogo = JogoAdivinhacao(1, 100)

    while not jogo.acertou:
        try:
            palpite = int(input('Digite seu palpite: '))
        except ValueError:
            exibicao.tentativa_invalida()
            continue

        resultado = jogo.registra_palpite(palpite)
        exibicao.dica(resultado)

    print(f'Você acertou em {jogo.tentativas} tentativa(s)!')