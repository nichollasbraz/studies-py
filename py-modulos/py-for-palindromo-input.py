frase = str(input("Digite uma frase:\n> ")).strip().upper()
fraseCont = frase.split()
fraseGrup = ''.join(fraseCont)
fraseInv = ''

for fLetra in range(len(fraseGrup) -1, -1, -1):
    fraseInv += fraseGrup[fLetra]

if fraseInv == fraseGrup:
    print(
        f"'{fraseGrup}' '{fraseInv}'\n"
        "É um palíndromo."
        )
else:
    print(
        f"'{fraseGrup}' '{fraseInv}'\n"
        "Não é um palíndromo."
        )
    