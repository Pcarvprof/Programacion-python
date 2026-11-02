# Definir una lista de números
numeros = [4, 2, 7, 4, 9, 4, 1, 4]
numero = int(input("Introduce un número: "))

contador = 0

for n in numeros:
    if n == numero:
        contador += 1

# Mostrar el resultado
print(f"El número {numero} aparece {contador} veces en la lista.")