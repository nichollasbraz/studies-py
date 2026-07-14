import os

def limparTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def valoresInf():
   contadorValores = 0
   numSum = 0
   msg = "digite um número\n"

   while True:
    limparTerminal()
    num = int(input(
      f"{msg}"
      "[999] parar\n"
      "> "
    ))

    if num != 999:
        numSum += num
        contadorValores += 1
        msg = f"último número: {num}\n"
        continue
    else:
        limparTerminal()
        print(
        f"números contados: {contadorValores}\n"
        f"soma dos números: {numSum}."
        )
        break

valoresInf()
