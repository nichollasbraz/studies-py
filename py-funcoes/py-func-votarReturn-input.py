def votar(ano):
    from datetime import date
    hoje = date.today().year
    idade = hoje - ano

    if idade >= 1 and idade < 17:
        return f"candidato tem {idade} anos.\nvoto não permitido."
            
    elif 16 <= idade < 18 or idade > 65:
        return f"candidato tem {idade} anos.\nvoto facultativo."
    
    else:
        return f"candidato tem {idade} anos.\nvoto obrigatório."

nasc = int(input("em qual ano você nasceu?\n> "))
print(votar(nasc))
