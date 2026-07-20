lanche = ('Pudim','Hambúrguer','Suco','Refrigerante','Pizza')

for c in lanche:
    print(
        "eu vou comer:\n"
        f"{c}", end=""
        ", " if c < lanche else ""
        )
