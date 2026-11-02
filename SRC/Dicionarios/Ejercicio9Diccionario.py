# Definir un diccionario con valores numéricos
diccionario = {
    "a": 10,
    "b": 25,
    "c": 3,
    "d": 18
}

clave_mayor_valor = None
mayor_valor = None

for clave, valor in diccionario.items():
    if mayor_valor is None or valor > mayor_valor:
        mayor_valor = valor
        clave_mayor_valor = clave

print(f"La clave con el valor más alto es: {clave_mayor_valor}")