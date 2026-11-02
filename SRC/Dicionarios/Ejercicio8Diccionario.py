# Definir un diccionario con valores numéricos
diccionario = {
    "a": 5,
    "b": 12,
    "c": 3,
    "d": 7
}

suma_total = 0

for valor in diccionario.values():
    suma_total += valor

print(f"La suma de los valores es: {suma_total}")