from math import sqrt, floor

num = int(input("Digite um número inteiro para calcular sua raiz quadrada: "))
raiz = sqrt(num)

print("Raiz quadrada de {} é: {:.3f}".format(num, floor(raiz)))
