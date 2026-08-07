from time import sleep
from random import randint

def randNums(lista):
    print("números sorteados: ", end="")
    for _ in range(0, 5):
        randNum = randint(1, 10)
        lista.append(randNum)
        print(f"{randNum}", end=" ", flush=True)
        sleep(0.5)
    print()

def sumSort(lista):
    sumNums = 0

    for num in lista:
        if num % 2 == 0:
            sumNums += num

    if sumNums == 0:
        print("não há números pares.")
    else:    
        print("números pares: ", end="")
        for num in lista:
            if num % 2 == 0:
                print(f"{num}", end=" ", flush=True)
                sleep(0.5)
        print(f"\nsoma: {sumNums}")

nums = []
randNums(nums)
sumSort(nums)
