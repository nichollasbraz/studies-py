def votar(ano):
    from datetime import date
    hoje = date.today().year
    idade = hoje - ano

    if idade >= 1 and idade < 17:
        print(
            f"candidato tem {idade} anos.\n"
            f"voto não permitido."
              ) 
    if idade == 17 or idade > 75:
        print(
            f"candidato tem {idade} anos.\n"
            f"voto facultativo."
        )
    if idade > 17 and idade <= 75:
        print(
            f"candidato tem {idade} anos.\n"
            f"voto obrigatório."
        )

votar(1930)
