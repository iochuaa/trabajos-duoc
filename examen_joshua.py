precio = 0
productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['Acer ', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {'8475HD': [387990, 10], '2175HD': [327990, 4], 'JjfFHD': [424990, 1],
         'fgdxFHD': [664990, 21], '123FHD': [290890, 32], '342FHD': [444990, 7],
         'GF75HD': [749990, 2], 'UWU131HD': [349990, 1], 'FS1230HD': [249990, 0],
         }


def mostrar_stock(marca):
    lista = []
    for clave, valor in productos.items():
        if valor[0] == marca:
            total = 0
            lista.append(clave)
            for cod, datos in stock.items():
                if cod in lista:
                    total = total+datos[1]
    print('El stock es:', total)


def busqueda_por_precio():
    precio_minimo = int(input("Ingrese precio minimo $ "))
    precio_maximo = int(input("Ingrese precio maximo $ "))


def listado_de_productos():
    for clave, valor in productos.items():
    print('-----listado de notebooks-----')
    print(f'{valor[0]} {valor[1]} {valor[2]} {valor[4]}')


while True:
    print('''
\nMENÚ PRINCIPAL PYbooks
====================================
1. stock de la marca
2. busqueda por precio del producto
3. listado de los productos
4. Salir
 ''')
    opcion = input("Seleccione una opción: ")
    if opcion == '1':
    mostrar_stock()
    elif opcion == '2':
    busqueda_por_precio()
    elif opcion == '3':
    listado_de_productos()
    elif opcion == '4':
    print("programa finalizado.")
    break
    else:
    print("Opción no válida. Intente nuevamente.")
