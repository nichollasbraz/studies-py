notas = {'Fulano de Tal':3,
         'Douglas Souza':9,
         'Thalys Nogueira':8,
         'ChatGPT':10,
         'Justin Bieber':4,
         'Claude Code':10,
         'Senhor Armani':2,
         'Pedro Henrique':1
        }

def alunosAprovados(notas):
    aprovados = []

    for aluno in notas:
        if notas[aluno] >= 9:
            aprovados.append(aluno)

    return sorted(aprovados)

print("Alunos aprovados:\n{}".format(alunosAprovados(notas)))
