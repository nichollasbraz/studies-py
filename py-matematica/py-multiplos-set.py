mult3 = set()
mult5 = set()
mult7 = set()

for n in range(110):
    if n % 3 == 0:
        mult3.add(n)

    if n % 5 == 0:
        mult5.add(n)

    if n % 7 == 0:
        mult7.add(n)

mult35 = mult5 & mult7
mult105 = mult3 & mult5 & mult7
mult3or7 = mult3 | mult7
mult3nor7 = mult3 ^ mult7
mult7not3 = mult7 - mult3

print("Múltiplos de 35: {}".format(sorted(mult35)))
print("Múltiplos de 105: {}".format(sorted(mult105)))
print("Múltiplos de 3 ou 7: {}".format(sorted(mult3or7)))
print("Múltiplos de 3 ou 7, mas não ambos: {}".format(sorted(mult3nor7)))
print("Múltiplos de 7 que não estão em 3: {}".format(sorted(mult7not3)))
