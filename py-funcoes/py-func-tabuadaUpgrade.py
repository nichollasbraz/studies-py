def tabuadaUpgrade(num):
    for i in range(1, 11):
        mult = i * num
        print(f"{num} x {i:2} = {mult}")
    
num = int(input("Insira um número:\n> "))
tabuadaUpgrade(num)
