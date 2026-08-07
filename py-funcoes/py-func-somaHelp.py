from time import sleep

def soma(a=0, b=0, c=0):
    """
    A função recebe três (03) parâmetros e realiza a soma.
    Caso não haja um valor determinado, o parâmetro é declarado automaticamente zero (0).
    """
    valores = [a, b, c]
    total = 0
    
    for i, num in enumerate(valores):
        if i < len(valores) - 1:
            print(f"{num}", end=" + ", flush=True) 
        else:
            print(f"{num}", end="", flush=True)
        sleep(0.5)
        total += num
    print()


    sleep(0.5)
    print(f"soma total: {total}")

help(soma)
soma(10,11,3)
soma(0,0,1)
    