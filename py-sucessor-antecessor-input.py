nome = (input("Nome do aluno: "))
nota_1 = int(input("Digite a primeira nota: "))
nota_2 = int(input("Digite a segunda nota: "))
med = (nota_1 + nota_2) / 2

print("\nAluno: {}".format(nome))
print("Média das notas {} e {}: {}".format(nota_1, nota_2, med))
