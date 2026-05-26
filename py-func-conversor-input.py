def area(largura, altura):
    area = largura * altura
    tinta = area / 2           
    
    print("\nDimensão da parede: {:.2f}x{:.2f}".format(largura, altura))
    print("Área: {:.2f}m²".format(area))
    print("Para cada 2m², será necessário {:.2f}l de tinta.".format(tinta))

    return area, tinta

largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))

area(largura,altura)
