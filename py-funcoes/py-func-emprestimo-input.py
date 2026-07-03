def Emprestimo():
    empCasa = float(input("Insira o valor do imóvel:\n> "))
    empSal = float(input("Insira sua renda mensal:\n> "))
    empAnos = float(input("Insira em quantos anos serão pagos:\n> "))

    if ((empCasa / empAnos) / 12) > (empSal * 0.30): 
        print("Infelizmente, sua renda não é suficiente.")
    else:
        print("Sua renda é compatível para manter por {} anos!".format(int(empAnos)))
    
Emprestimo()
