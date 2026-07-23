from random import randint

def randNums():
    while True:
        tuplaRand = (
            randint(1,9), randint(1,9), randint(1,9), randint(1,9), randint(1,9)
            )

        print("sequência randomizada:")
        for n in tuplaRand:
            print(f'{n} ', end="")

        print(
            f"\nmaior número: {max(tuplaRand)}\n"
            f"menor número: {min(tuplaRand)}")

        key = input("deseja recomeçar? [s/n]: ").upper()
        if key == 'S':
            continue
        else:
            break

randNums()
