pikachu_roll = 4500
otaku_roll = 5000
pulpo_roll = 5200
anguila_roll = 4800
pikachu = 0
otaku = 0
pulpo = 0
anguila = 0
dcto = 0.10
while True:
    print(' bienvenido a godzilla sushis')
    print('================================')
    print('1. pikachu roll ')
    print('2. otaku roll ')
    print('3. pulpo venenoso roll ')
    print('4. anguila elcetrica roll ')
    print('5. finalizar compra ')
    print('================================')
    opc = input('ingrese opcion de integrantes: ')
    if opc == '1':
        pikachu = pikachu+1
    elif opc == '2':
        otaku = otaku+1
    elif opc == '3':
        pulpo = pulpo+1
    elif opc == '4':
        anguila = anguila+1
        break
