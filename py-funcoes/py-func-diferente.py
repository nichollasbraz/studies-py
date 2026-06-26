
t = [[0,1,0],[1,0,1],[3,2,1,4]]

def diff(t):
    setNum = set()

    for line in t:
        for num in line:
            setNum.add(num)

    return len(setNum)

print(diff(t))