from datetime import datetime
from dateutil.relativedelta import relativedelta

def calcTempo(dia, mes, ano):
    dataAtual = datetime.now()
    dataNasc = datetime(ano, mes, dia)
    dataDiff = relativedelta(dataAtual, dataNasc)

    if dataDiff.years >= 18:
        print("Você pode se alistar!")

        dataMaior = dataNasc + relativedelta(years = 18)
        dataMaiorDiff = relativedelta(dataAtual, dataMaior)

        print(
            f"Já se passaram {dataMaiorDiff.years} anos, {dataMaiorDiff.months} meses e {dataMaiorDiff.days} dias desde que você atingiu a maioridade."
            )
    else:
        print("Você ainda é menor de idade e não pode se alistar.")

dia = int(input("Digite o dia em que você nasceu:\n> "))
mes = int(input("Digite o mês em que você nasceu:\n> "))
ano = int(input("Digite o ano em que você nasceu:\n> "))

calcTempo(dia, mes, ano)
