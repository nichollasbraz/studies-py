num = int(input("Digite um número de 1 a 9999: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

if num >= 1 and num <= 9999:
    print("\nAnalisando seu número...")
    if u >= 1:
        print("Unidade: {}".format(u))
    else:
        print("O número não possui unidades.")

    if d >= 1:
        print("Dezena: {}".format(d))
    else:
        print("O número não possui dezenas.")

    if c >= 1:
        print("Centena: {}".format(c))
    else:
        print("O número não possui centenas.")  

    if m >= 1:
        print("Milhar: {}".format(m))
    else:
        print("O número não possui milhares.")
else:
    print("\nNúmero inválido.")
