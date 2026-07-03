import random as rd


def sorteia_numero(inicio, fim):
    return rd.randint(inicio, fim)


def le_palpite():
    while True:
        try:
            palpite = int(input('Digite seu palpite: '))
            return palpite
        except ValueError:
            print('Entrada inválida. Digite um número inteiro.')


def mostra_dica(numero_secreto, palpite):
    if palpite < numero_secreto:
        print('O número é maior.')
    elif palpite > numero_secreto:
        print('O número é menor.')
    else:
        print('Parabéns! Você acertou!')


print('Bem-vindo ao jogo de Adivinhação!')
print('Tente adivinhar o número entre 1 e 100.\n')

numero_secreto = sorteia_numero(1, 100)
tentativas = 0

while True:
    palpite = le_palpite()
    tentativas = tentativas + 1

    mostra_dica(numero_secreto, palpite)

    if palpite == numero_secreto:
        print(f'Você acertou em {tentativas} tentativa(s)!')
        break

print('\nObrigado por jogar. Até a próxima!')