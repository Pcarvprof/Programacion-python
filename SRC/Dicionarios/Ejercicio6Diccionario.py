# Definir un diccionario de ejemplo
diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

diccionario_invertido = {valor: clave for clave, valor in diccionario.items()}

print("Diccionario invertido:", diccionario_invertido)