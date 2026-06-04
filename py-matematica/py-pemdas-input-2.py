num = int(input("Digite o primeiro valor inteiro: "))
num_2 = int(input("Digite o segundo valor inteiro: "))

pot = num ** num_2
exp = num * num_2
div = num / num_2
div_int = num // num_2
mod = num % num_2
add = (num + 5) + (num_2 + 5) 
sub = (num - 5) - (num_2 - 5) 

print("\nValores originais: {} e {}".format(num, num_2))
print("Potencializando {} por {}: {}".format(num, num_2, pot))
print("Multiplicando {} por {}: {}".format(num, num_2, exp))
print("Dividindo {} por {}: {}".format(num, num_2, div))
print("Dividindo {} por {} (inteiro): {}".format(num, num_2, div_int))
print("Módulo da divisão de {} por {}: {}".format(num, num_2, mod))
print("Adicionando 5 a cada valor e os somando: {}".format(add))
print("Diminuindo 5 a cada valor e os subtraindo: {}".format(sub))
