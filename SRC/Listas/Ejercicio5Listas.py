# Definir una lista con números repetidos
numeros = [1, 2, 2, 3, 4, 4, 5, 6, 6]
numeros_sin_repetidos = []

for numero in numeros:
    if numero not in numeros_sin_repetidos:
        numeros_sin_repetidos.append(numero)

print(f"Lista sin repetidos: {numeros_sin_repetidos}")