def Emprestimo():
    empCasa = float(input("Insira o valor do imóvel:\n> R$"))
    empSal = float(input("Insira sua renda mensal:\n> R$"))
    empAnos = float(input("Insira em quantos anos serão pagos:\n> "))
    empCasaPrest = (empCasa / empAnos) / 12
    empSalPrest = empSal * 0.3

    if empCasaPrest > empSalPrest: 
        print(f"A prestação do imóvel será de R${empCasaPrest:.2f} mensais.")
        print("Infelizmente, sua renda não é compatível.")
    else:
        print(f"A prestação do imóvel será de R${empCasaPrest:.2f} mensais")
        print(f"Sua renda é compatível!")
    
Emprestimo()
