listDummy = [19, 2, 3, 18, 23, 12]

print(f'original: {listDummy}')
listDummy.sort()
print(f'sorted: {listDummy}')
listDummy.insert(2, 0)
print(f'insert(2,0): {listDummy}')
listDummy.pop()
print(f'pop: {listDummy}')
listDummy.append(29)
print(f'append(29): {listDummy}')
print(f'\nessa é uma lista com {len(listDummy)} elementos.')
