import ast

def checkSorted(s):
    try:
        lista = list(ast.literal_eval(s))
    except Exception:
        lista = [i.strip() for i in s.strip('[]').split(',') if i.strip()]
    lista_srtd = sorted(lista)
    print("\nTrue" if lista == lista_srtd else "\nFalse")

checkSorted(input("Digite uma lista de objetos em []: "))
