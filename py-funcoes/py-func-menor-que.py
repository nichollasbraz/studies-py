def conversor(tam):    
    cm = tam * 100
    mm = tam * 1000
    convert_cm = print("\nEm centímetros: {:.2f}".format(cm))
    convert_mm = print("Em milímetros: {:.2f}".format(mm))
    return cm, mm

tam = float(input("Digite um valor em metros para ser convertido: "))
conversor(tam)