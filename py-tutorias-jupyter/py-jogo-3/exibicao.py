# exibicao.py
def boas_vindas():
    print('Bem-vindo ao jogo de Adivinhação!')
    print('Tente adivinhar o número entre 1 e 100.\n')

def dica(resultado):
    if resultado == 'maior':
        print('O número é maior.')
    elif resultado == 'menor':
        print('O número é menor.')
    else:
        print('Parabéns! Você acertou!')

def despedida():
    print('\n👋 Obrigado por jogar. Até a próxima!')

def tentativa_invalida():
    print('Entrada inválida. Digite um número inteiro.')