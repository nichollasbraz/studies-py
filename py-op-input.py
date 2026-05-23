num_1 = int(input("Digite um número inteiro: "))
num_2 = int(input("Digite um segundo número inteiro: "))
num_3 = float(input("Digite um numero decimal: "))

frst = num_1 * (num_2 / 2)
scnd = float(num_2 + (num_1 * num_3))
thrd = num_3 ** 3

print("\nPrimeira operação: {}".format(frst))
print("Segunda operação: {}".format(scnd))
print("Terceira operação: {:;2f}".format(thrd))
