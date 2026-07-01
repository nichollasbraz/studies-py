def valores():
    tentativas = 0
    soma = 0

    while True:
        try:
            num = float(input("Digite um número:\n> "))

            tentativas = 0      

            if num == 0:
                return soma

            soma += num

        except ValueError:
            print("Erro. Digite outro número.")
            tentativas += 1

            if tentativas == 2:
                print("Dois erros seguidos. Programa encerrado.")
                return
            
print(valores())