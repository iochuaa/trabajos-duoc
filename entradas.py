funcion_viernes = []
max_viernes = 150
funcion_sabado = []
max_sabado = 180

# === Comprar ===


def comprar():
    # Conseguir nombre
    while True:
        nombre = input('Ingrese nombre de cliente: ')
        if nombre.isalpha():
            print()
            break
        else:
            print('[Error] Nombre no válido! Solo se aceptan letras.')

    # Conseguir funcion
    while True:
        print('''Seleccióna una función:
\t[1] Cats Día Viernes.
\t[2] Cats Día Sábado.
''')
        funcion = input('Opción: ')
        if funcion in ['1', '2']:
            print()
            break
        else:
            print('[Error] Opción no válida!')

    # Función del viernes
    if funcion == '1':
        if nombre in funcion_viernes:  # Checkear si el nombre ya está en la lista
            print('[Error] Este nombre ya está registrado para esta función.\n')
        elif len(funcion_viernes) >= max_viernes:  # Checkear si quedan entradas
            print('[Error] Ya no quedan entradas disponibles para esta función.\n')
        else:  # Comprar con exito!
            funcion_viernes.append(nombre)
            print('Entrada comprada con exito!\n')

    # Función del sábado
    if funcion == '2':
        if nombre in funcion_sabado:  # Checkear si el nombre ya está en la lista
            print('[Error] Este nombre ya está registrado para esta función.\n')
        elif len(funcion_sabado) >= max_sabado:  # Checkear si quedan entradas
            print('[Error] Ya no quedan entradas disponibles para esta función.\n')
        else:  # Comprar con exito!
            funcion_sabado.append(nombre)
            print('Entrada comprada con exito!\n')

# === Cambiar ===


def cambiar():
    # Conseguir nombre
    while True:
        nombre = input('Ingrese nombre de cliente a cambiar: ')
        if nombre.isalpha():
            print()
            break
        else:
            print('[Error] Nombre no válido! Solo se aceptan letras.')

    # Si el nombre no tiene ninguna entrada, error
    if nombre not in funcion_viernes and nombre not in funcion_sabado:
        print('[Error] Este usuario no tiene ninguna entrada que cambiar.\n')
    elif nombre in funcion_sabado and nombre in funcion_viernes:  # Si el nombre está en ambas funciónes, error
        print(
            '[Error] Este usuario tiene entradas en ambas funciónes. Cambio cancelado.\n')
    else:
        # Conseguir input de confirmación
        while True:
            print('''Desea cambiar de función?
\t[1] Sí.
\t[2] No.
''')
            change_opc = input('Opción: ')
            if change_opc in ['1', '2']:
                print()
                break
            else:
                print('[Error] Opción no válida!')

        # Cambiar de función
        if change_opc == '1':
            # Cambio de viernes a sábado
            if nombre in funcion_viernes and nombre not in funcion_sabado:
                print('Cambiando entrada de sábado a viernes...\n')
                if len(funcion_sabado) >= max_sabado:
                    print(
                        '[Error] No quedan entradas el sábado. Cambio cancelado.\n')
                else:
                    funcion_viernes.remove(nombre)
                    funcion_sabado.append(nombre)
                    print('Entrada cambiada con éxito!.\n')
            # Cambio de sábado a viernes
            elif nombre in funcion_sabado and nombre not in funcion_viernes:
                print('Cambiando entrada de sábado a viernes...\n')
                if len(funcion_viernes) >= max_viernes:
                    print(
                        '[Error] No quedan entradas el viernes. Cambio cancelado.\n')
                else:
                    funcion_sabado.remove(nombre)
                    funcion_viernes.append(nombre)
                    print('Entrada cambiada con éxito!.\n')

        else:
            print('Cambio cancelado.')


# === Mostrar Stock ===
def stock():
    print('Entradas disponibles:')
    print('\tViernes: ', max_viernes - len(funcion_viernes),
          'entradas disponibles de', max_viernes, 'entradas totales')
    print('\tSabado: ', max_sabado - len(funcion_sabado),
          'entradas disponibles de', max_sabado, 'entradas totales')
    print()

# === Salir ===


def salir():
    print('Programa terminando...\n')

# === Main ===


def main():
    print()
    while True:
        print('''TOTEM AUTOATENCIÓN CAFECONLECHE
\t[1] Comprar entrada a Cats.
\t[2] Cambio de función.
\t[3] Mostrar stock de funciones.
\t[4] Salir.
''')
        opc = input('Opción: ')
        print()
        if opc == '1':
            comprar()
        elif opc == '2':
            cambiar()
        elif opc == '3':
            stock()
        elif opc == '4':
            salir()
            break
        else:
            print('[Error] Opción no válida!\n')


if __name__ == "__main__":
    main()
