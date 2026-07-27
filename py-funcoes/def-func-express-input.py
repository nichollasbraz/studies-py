def express():
    expressao = str(input("> "))
    pList = []

    for p in expressao:
        if p == '(':
            pList.append(p)
        elif p == ')':
            if len(pList) > 0:
                pList.pop()
            else:
                pList.append(p)
                break

    if len(pList) == 0:
        print("expressão devidamente aplicada")
    else:
        print("expressão equivocada")

express()
