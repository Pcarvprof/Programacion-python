# Definir un diccionario con números enteros
numeros = {
    "a": 5,
    "b": -3,
    "c": 8,
    "d": -1
}

claves_a_eliminar = [clave for clave, valor in numeros.items() if valor < 0]

for clave in claves_a_eliminar:
    del numeros[clave]

print("Diccionario sin valores negativos:", numeros)