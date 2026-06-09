num = int(input("Digite um número de 1 a 9999: "))

if 1 <= num <= 9999:
    u = num // 1 % 10
    d = num // 10 % 10
    c = num // 100 % 10
    m = num // 1000 % 10

    print("\nAnalisando seu número...")
    print("Unidade: {}".format(u))
    print("Dezena: {}".format(d))
    print("Centena: {}".format(c))
    print("Milhar: {}".format(m))
else:
    print("\nNúmero inválido.")