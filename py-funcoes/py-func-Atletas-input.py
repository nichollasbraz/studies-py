from datetime import datetime
from dateutil.relativedelta import relativedelta

def Atletas(dia, mes, ano):
    dataAtual = datetime.now()
    dataNasc = datetime(ano, mes, dia)
    dataDiff = relativedelta(dataAtual, dataNasc)
    
    print(f"O atleta tem {dataDiff.years} anos.")
    if dataDiff.years <= 9:
        print(f"Classificação: mirim")
    elif dataDiff.years > 9 and dataDiff.years <= 14:
        print(f"Classificação: infantil")
    elif dataDiff.years > 14 and dataDiff.years <= 19:
        print(f"Classificação: júnior")
    elif dataDiff.years > 19 and dataDiff.years <= 25:
        print(f"Classificação: sênior")
    elif dataDiff.years > 25:
        print(f"Classificação: master")
    else:
        print("Idade inválida.")
        
dia = int(input("Insira o dia em que o atleta nasceu:\n> "))
mes = int(input("Insira o mês em que o atleta nasceu:\n> "))
ano = int(input("Insira o ano em que o atleta nasceu:\n> "))

Atletas(dia, mes, ano)
