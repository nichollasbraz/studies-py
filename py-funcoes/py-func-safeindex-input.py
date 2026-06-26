lst = [30, 20, 40, 50]

def safeIndex(lst, valor):
    for i in range(0, len(lst)):
        if lst[i] == valor:
            return i
        
    print(f"O valor {valor} não está na lista.")
    return None

valor = (int(input("Digite um valor:\n> ")))
print(safeIndex(lst, valor))
