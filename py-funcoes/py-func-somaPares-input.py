def somaPares():
    soma = 0
    
    for i in range(0, 6):
        num = int(input(f"Digite seis números ({i+1} de 6):\n> "))
        
        if num % 2 == 0:
            soma += num       
        elif num % 2 > 0:
            print("Números ímpares não são permitidos.")
            continue
        
    print("Soma dos números pares:")
    print(soma)
    
somaPares()