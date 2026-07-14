def fibonacci():
    numFib = int(input("digite quantos termos serão mostrados:\n> "))
    termUm = 0
    termDois = 1 
    contFib = 3

    print(f"{termUm} ➝  {termDois} ➝  ", end="")
    while contFib <= numFib:
        termTres = termUm + termDois
        print(
            f"{termTres}", end=""
            f" ➝  " if contFib < numFib else ""
            )
        termUm = termDois
        termDois = termTres
        contFib += 1
    
fibonacci()
