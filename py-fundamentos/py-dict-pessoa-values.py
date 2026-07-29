estadoDict = {}
brasilLst = []

for _ in range(0,3):
    estadoDict['ES'] = str(input("Estado:\n> "))
    estadoDict['UF'] = str(input("Unidade Federativa (UF):\n> "))
    brasilLst.append(estadoDict.copy())

for e in brasilLst:
    for c, v in e.items():    
        print(f"{c} : {v}")
