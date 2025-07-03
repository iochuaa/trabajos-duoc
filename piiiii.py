edad = int(input('edad: '))
salario = int(input=('salario (USD): '))

if edad < 25 and salario > 2000:
    rep = input('Estas trabajando en una reconocida? y/n')
    if rep == 'y':
        print('puede solicitar')
    else:
        print('debe esperar')
elif edad >= 25:
    anos_exp = int(input('años de experiencia: '))
    if (salario > 3000 or anos_exp >= 5):
        print('puede solicitar')
