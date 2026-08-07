from time import sleep

valores = {
    "valores": [],
    "valor maior": None,
    "valor menor": None
}

def analyzer(valor):
    valores['valores'].append(valor)

    if valores['valor maior'] is None or valor > valores['valor maior']:
        valores['valor maior'] = valor

    if valores['valor menor'] is None or valor < valores ['valor menor']:
        valores['valor menor'] = valor


while True:
    valor = int(input("informe-me um valor:\n[-1] sair\n> "))

    if valor == -1:
        if len(valores['valores']) == 0:
                print("não foram inseridos valores.")
                sleep(1)
                break
        else:
            for num in valores['valores']:
                print(f"{num}", end=" ", flush=True)
                sleep(1)

            print(f"\nvalores inseridos: {len(valores['valores'])}")
            sleep(1)
            print(f"menor valor: {valores['valor menor']}")
            sleep(1)
            print(f"maior valor: {valores['valor maior']}")
            sleep(1)
            print("TYBG")
            sleep(1)
            break
    
    analyzer(valor)

    
