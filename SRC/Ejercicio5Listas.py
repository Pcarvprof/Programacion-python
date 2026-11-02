# Definir una lista con números repetidos
numeros = [1, 2, 2, 3, 4, 4, 5, 6, 6]

# Crear una nueva lista sin duplicados
numeros_sin_repetidos = []

# Añadir solo los números que no están ya en la nueva lista
for numero in numeros:
    if numero not in numeros_sin_repetidos:
        numeros_sin_repetidos.append(numero)

# Mostrar la lista sin elementos repetidos
print(f"Lista sin repetidos: {numeros_sin_repetidos}")