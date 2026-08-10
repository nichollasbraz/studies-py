def relatorio(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = "ótima"
        elif r['média'] >= 5:
            r['situação'] = "ok"
        else:
            r['situação'] = "ruim"

    return r 


print(relatorio(8.3,8.1,2.3))
