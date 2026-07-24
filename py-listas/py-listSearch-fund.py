listSearch = []
for contador in range(0, 5):
    chave = int(input("informe-me um valor: "))
    listSearch.append(chave)

for c, v in enumerate(listSearch):
    print(f"encontrado '{v}' na posição '{c}'")

listSearch.sort()
print(f"leitura finalizada.\nordem lexicográfica: {listSearch}",end="")
