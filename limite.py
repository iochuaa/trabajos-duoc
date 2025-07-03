import random
pi = 3.1416
while True:
    try:
        numinf = int(input('ingrese el limite inferior: '))
        break
    except:
        print('el limite inferior debe ser un entero!!!')
while True:
    try:
        numsup = int(input('ingrese el limite superior: '))
        if numsup > numinf:
            break
        else:
            print('El límite superior debe ser mayor al límite inferior!!!')
    except:
        print('el limite superior debe ser un entero!!!')
num = 6  # random.randint(numinf, numsup)
cantidad_cumple = 0
for i in range(num):
    while True:
        try:
            r = float(input('ingrese el radio en centimetros: '))
            break
        except:
            print('el radio debe ser un numero!!!')
    p = 2*r*pi
    if p >= 251 and p <= 283:
        cantidad_cumple = cantidad_cumple+1
print(f'la cantidad de circunferencia analizadas es= {num}')
print(f'la cantidad de circunferencia que cumple es= {cantidad_cumple}')
print(f'la cantidad de circunferencia que no cumple es= {num-cantidad_cumple}')
