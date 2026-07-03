# frontend.py
import random
import exibicao

def jogar():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while True:
        try:
            palpite = int(input("Digite seu palpite: "))
        except ValueError:
            exibicao.tentativa_invalida()
            continue

        tentativas += 1
        exibicao.dica(numero_secreto, palpite)

        if palpite == numero_secreto:
            print(f"Você acertou em {tentativas} tentativa(s)!")
            break