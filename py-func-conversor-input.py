def conversor(tam):      
    km = tam / 1000
    hm = tam / 100
    dam = tam / 10    
    dm = tam * 10
    cm = tam * 100
    mm = tam * 1000
    
    c_km = print("\nEm quilômetros: {:.4f} km".format(km))
    c_hm = print("Em hectômetros: {:.3f} hm".format(hm))
    c_dam = print("Em decâmetros: {:.2f} dam".format(dam))
    c_dm = print("Em decímetros: {:.0f} dm".format(dm))
    c_cm = print("Em centímetros: {:.0f} cm".format(cm))
    c_mm = print("Em milímetros: {:.0f} mm".format(mm))
    return cm, mm

tam = float(input("Digite um valor em metros para ser convertido: "))
conversor(tam)
