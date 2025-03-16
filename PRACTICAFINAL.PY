# Programa de gestión de inventario

def agregar_producto(inventario, nombre, cantidad, precio):
    """Agrega un producto al inventario o actualiza su cantidad y precio."""
    if nombre in inventario:  # Si el producto ya existe en el inventario
        inventario[nombre]['cantidad'] += cantidad  # Suma la cantidad ingresada a la existente
        inventario[nombre]['precio'] = precio  # Actualiza el precio del producto
    else:
        inventario[nombre] = {'cantidad': cantidad, 'precio': precio}  # Agrega un nuevo producto al inventario

def mostrar_inventario(inventario):
    """Muestra el inventario completo."""
    print("\nInventario Actual:")
    for nombre, info in inventario.items():  # Itera sobre cada producto en el inventario
        print(f"Producto: {nombre}, Cantidad: {info['cantidad']}, Precio: ${info['precio']:.2f}")  # Muestra la información

def vender_producto(inventario, nombre, cantidad):
    """Reduce la cantidad de un producto al venderlo."""
    if nombre in inventario and inventario[nombre]['cantidad'] >= cantidad:  # Verifica si el producto existe y si hay suficiente stock
        inventario[nombre]['cantidad'] -= cantidad  # Resta la cantidad vendida
        print(f"Se vendieron {cantidad} unidades de {nombre}.")
        if inventario[nombre]['cantidad'] == 0:  # Si el producto se agota, se elimina del inventario
            del inventario[nombre]
            print(f"{nombre} se ha agotado y fue eliminado del inventario.")
    else:
        print("Stock insuficiente o producto no encontrado.")  # Mensaje de error si no hay suficiente stock o el producto no existe

def buscar_producto(inventario, nombre):
    """Busca un producto en el inventario y muestra su información."""
    if nombre in inventario:  # Verifica si el producto existe en el inventario
        info = inventario[nombre]  # Obtiene la información del producto
        print(f"Producto: {nombre}, Cantidad: {info['cantidad']}, Precio: ${info['precio']:.2f}")  # Muestra la información
    else:
        print("Producto no encontrado.")  # Mensaje si el producto no está en el inventario

def calcular_valor_total(inventario):
    """Calcula el valor total del inventario."""
    total = sum(info['cantidad'] * info['precio'] for info in inventario.values())  # Suma el valor total de todos los productos
    print(f"Valor total del inventario: ${total:.2f}")  # Muestra el valor total

def menu():
    """Menú de opciones para el usuario."""
    inventario = {}  # Diccionario para almacenar los productos del inventario
    while True:  # Ciclo infinito hasta que el usuario elija salir
        print("\nOpciones:")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Vender producto")
        print("4. Buscar producto")
        print("5. Calcular valor total")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")  # Solicita una opción al usuario
        
        if opcion == '1':  # Opción para agregar producto
            nombre = input("Nombre del producto: ")  # Solicita el nombre del producto
            cantidad = int(input("Cantidad: "))  # Solicita la cantidad del producto
            precio = float(input("Precio: "))  # Solicita el precio del producto
            agregar_producto(inventario, nombre, cantidad, precio)  # Llama a la función para agregar el producto
        elif opcion == '2':  # Opción para mostrar el inventario
            mostrar_inventario(inventario)
        elif opcion == '3':  # Opción para vender producto
            nombre = input("Nombre del producto: ")  # Solicita el nombre del producto
            cantidad = int(input("Cantidad a vender: "))  # Solicita la cantidad a vender
            vender_producto(inventario, nombre, cantidad)  # Llama a la función para vender el producto
        elif opcion == '4':  # Opción para buscar un producto
            nombre = input("Nombre del producto a buscar: ")  # Solicita el nombre del producto a buscar
            buscar_producto(inventario, nombre)  # Llama a la función para buscar el producto
        elif opcion == '5':  # Opción para calcular el valor total del inventario
            calcular_valor_total(inventario)
        elif opcion == '6':  # Opción para salir del programa
            print("Saliendo del programa.")
            break  # Termina el ciclo y cierra el programa
        else:
            print("Opción no válida, intente de nuevo.")  # Mensaje de error si la opción ingresada no es válida

# Ejecutar el programa
menu()  # Llama a la función del menú para iniciar el programa