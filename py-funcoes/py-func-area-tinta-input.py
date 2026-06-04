def conversor_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    
    print("\nValor convertido: {:.2f}°F".format(fahrenheit))

    return fahrenheit

celsius = float(input("Digite o valor em °C para conversão em °F: "))

conversor_fahrenheit(celsius)