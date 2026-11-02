# Definir un diccionario de productos y precios
productos = {
    "pan": 1.20,
    "leche": 0.99,
    "huevos": 2.50
}

producto = input("Introduce el nombre del producto: ")
precio = float(input(f"Introduce el nuevo precio de {producto}: "))

productos[producto] = precio

print("Diccionario de productos y precios actualizado:", productos)