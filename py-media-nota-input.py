nome = (input("Nome do aluno: "))
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_final = (nota_1 + nota_2) / 2

print("\nAluno: {}".format(nome))
print("Nota final: {:.1f}".format(nota_final))
