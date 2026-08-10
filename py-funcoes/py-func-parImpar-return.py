def parImpar(num=0):
    if num % 2 == 0:
        return True
    else:
        return False


num = int(input("informe-me um número:\n> "))

if parImpar(num):
    print("é par!")
else:
    print("é ímpar!")
