import random

n = 4

def game(n):
  for i in range(n):
    x = random.randint(0,9)
    y = random.randint(0,9)
    print('{} + {} = ?'.format(x,y))
    
    try:
        resp = int(input('Digite o valor da soma: '))
        
        if resp == (x+y):
            print('Correto')
        else:
            print('Errado')

    except ValueError:
       print("Entrada inválida")
       continue 

game(n)