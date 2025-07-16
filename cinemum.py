ventas = [
    {"numero": 2001, "fecha": "05/07/2025",
        "cliente": "Daniela Fuentes", "total": 0},
    {"numero": 2002, "fecha": "06/07/2025",
        "cliente": "Ignacio Morales", "total": 0},
    {"numero": 2003, "fecha": "07/07/2025", "cliente": "Camila Soto", "total": 0},
    {"numero": 2004, "fecha": "08/07/2025",
        "cliente": "Luis Contreras", "total": 0},
    {"numero": 2005, "fecha": "09/07/2025",
        "cliente": "Valentina Reyes", "total": 0},
]
entradas = [
    {"numero_boleta": 2001, "pelicula": "Spiderman",
        "cantidad": 2, "precio_unitario": 4000},
    {"numero_boleta": 2001, "pelicula": "Frozen",
        "cantidad": 1, "precio_unitario": 3500},

    {"numero_boleta": 2002, "pelicula": "Batman",
        "cantidad": 3, "precio_unitario": 4500},

    {"numero_boleta": 2003, "pelicula": "Avatar",
        "cantidad": 2, "precio_unitario": 5000},
    {"numero_boleta": 2003, "pelicula": "Frozen",
        "cantidad": 1, "precio_unitario": 3500},

    {"numero_boleta": 2004, "pelicula": "Spiderman",
        "cantidad": 1, "precio_unitario": 4000},

    {"numero_boleta": 2005, "pelicula": "Avatar",
        "cantidad": 2, "precio_unitario": 5000},
    {"numero_boleta": 2005, "pelicula": "Batman",
        "cantidad": 1, "precio_unitario": 4500},
]
peliculas_validas = ["Spiderman", "Frozen", "Batman", "Avatar", "Mario Bros"]


def detalle_completo(num, pelicula, cliente):
    for venta in ventas:
        if venta["numero"] == num:
            print(f"numero boleta: {venta["numero"]} -- cliente: {cliente} -- fecha:{venta["fecha"]}")
            print('pelicula compradas: ')

            for entrada in entradas:
                if entrada['numero_boleta'] == num:
                    subtotal = entrada['cantidad'] * entrada['precio unitario']
                    print(f'pelicula: {entrada['pelicula']} -- cantidad:{venta['cantidad']} -- precio unitario $: {venta['precio_unitario']}')
                    return
                print('venta no encontrada ')


def buscar_num_boleta():
    for venta in ventas:
        if venta['numero'] == 'numero_boleta'


def actualizar_totales():
    for venta in ventas:
        total = 0
        for entrada in entradas:
            if entrada['numero_boleta'] == venta['numero']:
                total +=


def total_vendido():


def menu():
    print(' ----menu---- ')
    print('1.-Ver total vendido en un mes y año ')
    print('2.-Ver detalle completo de una boleta (cliente, películas, subtotales, total) ')
    print('3.-Agregar más entradas a una boleta ')
    print('4.-Actualizar los totales de todas las boletas ')
    print('5.-salir del sistema')


while True:
    menu()
    opc = input('ingrese una opcion: ')
    if opc == '1':
        total_vendido
    elif opc == '2':
        detalle_completo()
    elif opc == '3':
        print(' ')
    elif opc == '4':
        print(' ')
    elif opc == '5':
        print('usted salio del sistema ')
        break
    else:
        print('ingrese una opcion valida ')
