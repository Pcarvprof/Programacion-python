# Definir dos diccionarios
diccionario1 = {"a": 1, "b": 2, "c": 3}
diccionario2 = {"b": 4, "d": 5}

for clave, valor in diccionario2.items():
    diccionario1[clave] = valor

print("Diccionario combinado:", diccionario1)