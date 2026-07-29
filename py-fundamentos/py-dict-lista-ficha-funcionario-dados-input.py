from datetime import datetime

pessoaDict = {}
fichaLst = []

pessoaDict['nome'] = str(input("nome:\n> "))

pessoaDict['idade'] = int(input("ano de nascimento:\n> "))
pessoaDict['idade'] = datetime.now().year - pessoaDict['idade'] 

pessoaDict['ctps'] = str(input("carteira de trabalho (0 não possui):\n> "))
if pessoaDict['ctps'] != '0':
    pessoaDict['aposentadoria'] = int(input("ano de contratação:\n> "))
    pessoaDict['aposentadoria'] = pessoaDict['aposentadoria'] + 65
    pessoaDict['salário'] = float(input("salário:\n> r$ "))
else:
    pessoaDict['ctps'] = 'não possui'

fichaLst.append(pessoaDict.copy())
pessoaDict.clear()

for dado in fichaLst:
    for c, v in dado.items():
        print(f"{c} : {v}")
