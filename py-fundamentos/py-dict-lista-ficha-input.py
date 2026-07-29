alunoDict = {}
fichaLst = []

alunoDict['nome'] = str(input("nome do aluno:\n> ")).lower()
alunoDict['média'] = float(input("média do aluno:\n> "))

if alunoDict['média'] >= 7:
    alunoDict['situação'] = 'aprovado(a)'
elif 5 <= alunoDict['média'] < 7: 
    alunoDict['situação'] = 'em recuperação'
else:
    alunoDict['situação'] = 'reprovado(a)'

fichaLst.append(alunoDict.copy())
alunoDict.clear()

for dados in fichaLst:
    for c, v in dados.items():
        print(f"{c} : {v}")
        