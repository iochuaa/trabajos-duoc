boletas = [
    {"numero": 1001, "fecha": "01/07/2025", "cliente": "Juan Pérez", "total": 0},
    {"numero": 1002, "fecha": "02/07/2025", "cliente": "María López", "total": 0},
    {"numero": 1003, "fecha": "03/07/2025", "cliente": "Carlos Soto", "total": 0},
    {"numero": 1004, "fecha": "04/07/2025", "cliente": "Ana Torres", "total": 0},
    {"numero": 1005, "fecha": "05/07/2025", "cliente": "Pedro Rojas", "total": 0},
    {"numero": 1006, "fecha": "06/07/2025", "cliente": "Laura Díaz", "total": 0},
    {"numero": 1007, "fecha": "07/07/2025",
        "cliente": "Felipe Gutiérrez", "total": 0},
    {"numero": 1008, "fecha": "08/07/2025", "cliente": "Sofía Morales", "total": 0},
    {"numero": 1009, "fecha": "09/07/2025", "cliente": "Andrés Bravo", "total": 0},
    {"numero": 1010, "fecha": "10/07/2025",
        "cliente": "Gabriela Méndez", "total": 0},
]

detalle = [
    {"numero_boleta": 1001, "producto": "Leche",
        "cantidad": 2, "precio_unitario": 1200},
    {"numero_boleta": 1001, "producto": "Pan",
        "cantidad": 1, "precio_unitario": 1500},
    {"numero_boleta": 1001, "producto": "Huevos",
        "cantidad": 1, "precio_unitario": 2500},
    {"numero_boleta": 1002, "producto": "Arroz",
        "cantidad": 1, "precio_unitario": 1800},
    {"numero_boleta": 1002, "producto": "Fideos",
        "cantidad": 2, "precio_unitario": 900},
    {"numero_boleta": 1003, "producto": "Aceite",
        "cantidad": 1, "precio_unitario": 3000},
    {"numero_boleta": 1003, "producto": "Azúcar",
        "cantidad": 1, "precio_unitario": 1500},
    {"numero_boleta": 1003, "producto": "Café",
        "cantidad": 1, "precio_unitario": 2500},
    {"numero_boleta": 1004, "producto": "Pan",
        "cantidad": 2, "precio_unitario": 1500},
    {"numero_boleta": 1004, "producto": "Sal",
        "cantidad": 1, "precio_unitario": 800},
    {"numero_boleta": 1005, "producto": "Jugo",
        "cantidad": 2, "precio_unitario": 1200},
    {"numero_boleta": 1005, "producto": "Leche",
        "cantidad": 1, "precio_unitario": 1200},
    {"numero_boleta": 1005, "producto": "Arroz",
        "cantidad": 1, "precio_unitario": 1800},
    {"numero_boleta": 1006, "producto": "Huevos",
        "cantidad": 1, "precio_unitario": 2500},
    {"numero_boleta": 1006, "producto": "Café",
        "cantidad": 1, "precio_unitario": 2500},
    {"numero_boleta": 1007, "producto": "Azúcar",
        "cantidad": 1, "precio_unitario": 1500},
    {"numero_boleta": 1007, "producto": "Fideos",
        "cantidad": 2, "precio_unitario": 900},
    {"numero_boleta": 1008, "producto": "Pan",
        "cantidad": 1, "precio_unitario": 1500},
    {"numero_boleta": 1008, "producto": "Sal",
        "cantidad": 1, "precio_unitario": 800},
    {"numero_boleta": 1008, "producto": "Aceite",
        "cantidad": 1, "precio_unitario": 3000},
    {"numero_boleta": 1008, "producto": "Jugo",
        "cantidad": 1, "precio_unitario": 1200},
    {"numero_boleta": 1009, "producto": "Leche",
        "cantidad": 2, "precio_unitario": 1200},
    {"numero_boleta": 1009, "producto": "Huevos",
        "cantidad": 1, "precio_unitario": 2500},
    {"numero_boleta": 1009, "producto": "Arroz",
        "cantidad": 1, "precio_unitario": 1800},
    {"numero_boleta": 1010, "producto": "Fideos",
        "cantidad": 2, "precio_unitario": 900},
    {"numero_boleta": 1010, "producto": "Café",
        "cantidad": 1, "precio_unitario": 2500},
]

productos_validos = ['Leche', 'Pan', 'Huevos', 'Arroz',
                     'Fideos', 'Aceite', 'Azúcar', 'Café', 'Sal', 'Jugo']


def menu():
    print("\nMENÚ PRINCIPAL SUPERMERCADO DUMBO")
    print("====================================")
    print("1. Total vendido en un mes y año")
    print("2. Información de una boleta")
    print("3. Agregar producto a una boleta")
    print("4. Actualizar total de todas las boletas")
    print("5. Salir")2
