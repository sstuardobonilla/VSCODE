def analizar_inventario(Inventario):

    print("Este es mi trabajo de Logica y Diseño")
    print("================================================")
    print(" INFORME DE CONTROL DE STOCK Y REPOSICION")
    print("================================================")

    # Estructura Ciclica (for)

    for producto in Inventario:
        nombre = producto["nombre"]
        actual = producto["actual"]
        minimo = producto["minimo"]

        # Estructura de Control Condicional (is-else)
        if actual < minimo:
            # Calculo de optimizacion de stock
            unidades_a_pedir = (minimo * 2) - actual
            print(f" [Alerta Critica] -> Producto: {nombre}")
            print(f"   Stock Actual: {actual} unidades | Stock Minimo: {minimo} unidades")
            print(f"   Recomendacion: Pedir {unidades_a_pedir} unidades para optimizar el stock.")
        else:
            print(f" [Estado Optimo] -> Producto: {nombre}")
            print(f"   Stock Actual: {actual} unidades | Estado: Seguro. \n")

    print("================================================")
    print(" Fin del Informe de Control de Stock y Reposicion")
    print("================================================")

# Estructura de Datos (Lista de Diccionarios)
Inventario_productos = [
    {"nombre": "Producto A", "actual": 5, "minimo": 10},
    {"nombre": "Producto B", "actual": 15, "minimo": 10},
    {"nombre": "Producto C", "actual": 8, "minimo": 12},
    {"nombre": "Producto D", "actual": 20, "minimo": 15},
    {"nombre": "Producto E", "actual": 3, "minimo": 5}
]

# Ejecucion del Programa
analizar_inventario(Inventario_productos)