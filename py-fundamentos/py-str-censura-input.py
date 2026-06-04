frase = input("Digite uma frase: ")
c_frase = frase.split()

p_frase = input("Digite uma palavra nova: ")
num = int(input("Digite a posição onde será inserida na frase original: "))
num -= 1

encontrou = False

if 0 <= num < len(c_frase):
    c_frase[num] = p_frase
    encontrou = True
else:
    print("\nA posição está inválida.")
    encontrou = False

r_frase = " ".join(c_frase)
print("\nFrase reajustada:\n{}".format(r_frase))
