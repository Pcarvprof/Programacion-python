numeros = [23, 56, 12, 89, 4]
mayor = numeros[0]

for numero in numeros:
    if numero > mayor:
        mayor = numero

print(f"El número mayor es: {mayor}")