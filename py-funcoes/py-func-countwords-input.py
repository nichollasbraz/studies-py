import unicodedata

def remover_acentos(texto):
    texto = texto.replace(".", "")
    texto = texto.replace(",", "")
    texto = texto.replace("!", "")
    texto = texto.replace("?", "")
    texto = texto.lower()
    texto = unicodedata.normalize("NFD", texto)

    resultado = ""
    for c in texto:
        if unicodedata.category(c) != "Mn":
            resultado += c
    
    return resultado

def wordCount(texto):
    lst_texto = texto.split()
    

    dic_contador = {}
    
    for lst_palavra in lst_texto:
        if lst_palavra in dic_contador:
            dic_contador[lst_palavra] += 1
        else:
            dic_contador[lst_palavra] = 1

    for lst_palavra in dic_contador:
        if dic_contador[lst_palavra] == 1:
            print("'{}' aparece {} vez.".format(lst_palavra, dic_contador[lst_palavra]))
        else:
            print("'{}' aparece {} vezes.".format(lst_palavra, dic_contador[lst_palavra]))

print("Insira uma frase ou texto:")
texto = input("> ").strip()

rA = remover_acentos(texto)
wC = wordCount(rA)
