a = eval(input('Digite o valor do número "A": '))
b = eval(input('Digite o valor do número "B": '))
c = eval(input('Digite o valor número "C": '))

if a < b:
    cond_1 = ("OK!")
else:
    cond_1 = ("Não!")

if c > b:
    cond_2 = ("OK!")
else:
    cond_2 = ("Não!")

if (a + b) == c:
    cond_3 = ("OK!")
else:
    cond_3 = ("Não!")

if (a ** 2 + b ** 2) == c ** 2:
    cond_4 = ("OK!")
else:
    cond_4 = ("Não!")

print("\nCondição 1 (A < B): {}".format(cond_1))
print("Condição 2 (C > B): {}".format(cond_2))
print("Condição 3 (A + B = C): {}".format(cond_3))
print("Condição 4: (A² + B² = C²): {}".format(cond_4))
