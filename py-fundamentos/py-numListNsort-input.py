numList = []

for i in range(0,5):
    num = int(input("informe-me um número\n> "))
    if i == 0:
        numList.append(num)
    else:
        c = 0
        while c < len(numList):
            if num <= numList[c]:
                numList.insert(c, num)
                break
        c += 1

print(f"lista: {numList}")
