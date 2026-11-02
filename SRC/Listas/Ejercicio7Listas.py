# Definir una lista de números
numeros = [5, 2, 9, 1, 7]

for i in range(len(numeros)):
    for j in range(0, len(numeros)-i-1):
        if numeros[j] > numeros[j+1]:
            numeros[j], numeros[j+1] = numeros[j+1], numeros[j]

print(f"Lista ordenada: {numeros}")