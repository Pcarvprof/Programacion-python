# Definir una lista con números positivos y negativos
numeros = [10, -5, 3, -7, 0, 8]

for i in range(len(numeros)):
    if numeros[i] < 0:
        numeros[i] = 0

print(f"Lista después de reemplazar negativos: {numeros}")