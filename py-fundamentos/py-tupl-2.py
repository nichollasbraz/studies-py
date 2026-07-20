lanche = ('Pudim','Hambúrguer','Suco','Refrigerante','Pizza')

print("eu vou comer:")
for c in lanche:
    print(f"{c}", end="")
    if c != lanche[-1]:
        print(", ", end="")
    