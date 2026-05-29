def average(quantidade):
    soma = 0.0
    
    for num in range(quantidade):
        nota = float(input("Digite a próxima nota: "))
        soma += nota
    
    return soma / quantidade

def judge(media):
    if media >= 7:
        print("O aluno foi aprovado! Parabéns!")
    else:
        print("O aluno foi reprovado.")

quantidade = int(input("Quantas notas serão inseridas? "))

media = average(quantidade)
print("\nMédia: {:.1f}".format(media))

cond = judge(media)


