city = str(input("Em qual cidade você nasceu? "))
city.strip()
city_u = city.upper()
correct_city = "SANTO"

if city_u[:5] == correct_city:
    print("\nLegal!")
else:
    print("\nNão")