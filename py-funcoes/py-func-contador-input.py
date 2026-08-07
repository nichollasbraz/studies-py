from time import sleep

def contador(init, final, passo):
    if init < final:
        cont = init
        while cont <= final:
            print(f"{cont}", end=" ", flush=True)
            sleep(0.5)
            cont += passo
        print("fim")
    else:
        cont = init
        while cont >= final:
            print(f"{cont}", end=" ", flush=True)
            sleep(0.5)
            cont -= passo
        print("fim")


contador(1, 10, 1)
contador(10, 0, 2)

print("sua vez!")
sleep(0.5)
init = int(input("digite um número inicial:\n> "))
final = int(input("digite um número final:\n> "))
passo = int(input("digite um passo:\n> "))

contador(init, final, passo)

sleep(0.5)
print("fechando programa...")
sleep(0.7)