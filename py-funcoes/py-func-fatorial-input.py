def fatorial(num):
    if num < 0:
        print("\nValor inválido!")
        return None
    
    result = 1
    
    print("\n", end="")
    for i in range(1, num + 1):
        print("{}".format(i), end="")
        if i < num:
            print(" * ", end="")
        result *= i

    print("\n!{}: {}".format(num, result))

num = int(input("Digite um número inteiro positivo: "))
fatorial(num)
