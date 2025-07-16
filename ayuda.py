

asistentes = {
    "A001": ["Ana Torres", "Concierto Rock", "15-03-2024"],
    "A002": ["Luis Perez", "Festival Jazz", "20-03-2024"],
    "A003": ["Maria Lopez", "Concierto Pop", "10-04-2024"],
    "A004": ["Carlos Gomez", "Festival Jazz", "25-03-2024"],
    "A005": ["Sofia Ramirez", "Concierto Rock", "01-05-2024"],
    "A006": ["Pedro Diaz", "Concierto Pop", "12-04-2024"],
    "A007": ["Laura Fernandez", "Festival Jazz", "30-03-2024"],
    "A008": ["Diego Soto", "Concierto Rock", "05-05-2024"],
    "A009": ["Elena Castro", "Concierto Pop", "18-04-2024"],
    "A010": ["Francisco Ruiz", "Festival Jazz", "02-04-2024"],
}


def menu():
    print(' ----menu---- ')
    print('1.-asistentes de evento ')
    print('2.-asistente por mes de registro ')
    print('3.-eliminar asistente ')
    print('4.-salir ')


def asistentes_de_evento():
    opc = input('ingrese el evento que quiere consultar: ')


while True:
    menu()
    opc = input('ingrese una opcion: ')
    if opc == '4':
        print('usted salio del menu ')
        break
    elif opc == '3':
        print('usted salio del menu ')
    elif opc == '2':
        print('usted salio del menu ')
    elif opc == '1':
        asistentes_de_evento()
        print('usted salio del menu ')
    else:
        print('usted salio del menu ')
