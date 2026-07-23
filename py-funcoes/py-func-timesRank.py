def timesRank():
    times = (
        'Palmeiras','Flamengo','Athletico-PR','Fluminense','Bragantino',
        'Bahia','Cruzeiro','Coritiba','São Paulo','Botafogo',
        'Atlético-MG','EC Vitória','Corinthians','Internacional','Santos',
        'Grêmio', 'Vasco da Gama','Mirassol','Remo','Chapecoense'
        )

    print(
        'primeiros colocados do Brasileirão:\n'
        f'{times[0:5]}\n'
        'últimos colocados do Brasileirão:\n'
        f'{times[-4:]}\n'
        'colocados em ordem lexicográfica:\n'
        f'{sorted(times)}\n'
        'colocação do time da Chapecoense:\n'
        f'{times.index("Chapecoense") + 1}'
        )

timesRank()
    