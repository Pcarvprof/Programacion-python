# Definir un diccionario de frutas y colores
frutas_colores = {
    "manzana": "rojo",
    "platano": "amarillo",
    "pera": "verde",
    "naranja": "naranja"
}

fruta = input("Introduce el nombre de una fruta: ")

if fruta in frutas_colores:
    print(f"El color de la {fruta} es: {frutas_colores[fruta]}")
else:
    print("Esa fruta no está en el diccionario.")