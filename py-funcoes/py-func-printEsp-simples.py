def printEsp(msg):
    tam = len(msg) + 4
    print("~" * tam)
    print(f"  {msg}")
    print("~" * tam)


printEsp('test')
