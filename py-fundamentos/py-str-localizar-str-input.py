frase = str(input("Escreva uma frase: ")).strip()
frase = frase.upper()

print("\nAnalisando seu texto...")
print("A letra 'A' apareceu {} vezes.".format(frase.count("A")))
print("Primeira aparição: posição {}.".format(frase.find("A")+1))
print("Última aparição: posição {}".format(frase.rfind("A")+1))
