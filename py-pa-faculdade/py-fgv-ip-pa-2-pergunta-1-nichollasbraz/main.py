t = [[0,21,0],[1,7,31],[31,2,1,4]]

def diferente(t):
    setNum = set()

    for linha in t:
        for num in linha:
            setNum.add(num)

    return len(setNum)

print(diferente(t))