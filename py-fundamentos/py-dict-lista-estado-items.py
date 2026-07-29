estadoDict = {}
brasilLst = []

for _ in range(0,3):
    estadoDict['ES'] = str(input("Estado:\n> "))
    estadoDict['UF'] = str(input("Unidade Federativa (UF):\n> "))
    brasilLst.append(estadoDict.copy())

for e in brasilLst:
    for v in e.values():    
        print(f"{v} : {v}")
