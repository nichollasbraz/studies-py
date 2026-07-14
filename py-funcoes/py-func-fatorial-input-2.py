def fatorial(num):
    fat = 1
    i = num
    
    print(f"{num}! = ", end="")
    while i > 0:
        print(f"{i}", end="")
        print(f" x " if i > 1 else " = ", end="")
        fat *= i
        i -= 1
    print(f"{fat}")

num = int(input("digite um número:\n> "))
fatorial(num)
