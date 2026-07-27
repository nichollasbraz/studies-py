pessList = list()
totalList = list()
pesoMaior = pesoMenor = 0

while True:
    pessList.append(input("informe-me um nome\n> "))
    pessList.append(float(input("informe-me o peso\n> ")))

    if len(totalList) == 0:
        pesoMaior = pesoMenor = pessList[1]
    else:
        if pessList[1] > pesoMaior:
            pesoMaior = pessList[1]
        if pessList[1] < pesoMenor:
            pesoMenor = pessList[1]

    totalList.append(pessList[:])
    pessList.clear()

    key = input("continuar? [s/n]\n> ").lower()
    if key == 's':
        continue
    else:      
        print("maiores pesos:", end=" ")
        for pessoa in totalList:
            if pessoa[1] == pesoMaior:
                print(pessoa[0], end=" ")
        print(f"com {pesoMaior:.2f} kgs")

        print("menores pesos:", end=" ")
        for pessoa in totalList:
            if pessoa[1] == pesoMenor:
                print(pessoa[0], end=" ")
        print(f"com {pesoMenor:.2f} kgs")
    break
