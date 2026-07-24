def MaiorMenor():
    listMm = []
    nMaior = 0
    nMenor = 0

    for n in range(0, 5):
        listMm.append(int(input("informe-me um número: ")))

        if n == 0:
            nMaior = nMenor = listMm[n]
        else:
            if listMm[n] > nMaior:
                nMaior = listMm[n]
            elif listMm[n] < nMenor:
                nMenor = listMm[n]

    print(f"lista: {listMm}")
    print(f"maior número: {nMaior} na posição", end="")

    for i, v in enumerate(listMm):
        if listMm[i] == nMaior:
            print(f' {i}')

    print(f"menor número: {nMenor} na posição", end="")

    for i, v in enumerate(listMm):
        if listMm[i] == nMenor:
            print(f' {i}')

MaiorMenor()
