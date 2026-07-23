lanche = ('Pudim','Hambúrguer','Suco','Refrigerante','Pizza')

print("eu vou comer:")

for i in range(0, len(lanche)):
    print(f"{lanche[i]}", end="")
    if i < len(lanche) - 2: 
        print(", ", end="")
    if i == len(lanche) - 2:
        print(" e ", end="")
    if i == len(lanche) - 1:
        print(".", end="")

# for c in lanche:
#    print(f"{c}", end="")
#    if c != lanche[-1]:
#       print(", ", end="")
#    else:
#      print(".", end="")
