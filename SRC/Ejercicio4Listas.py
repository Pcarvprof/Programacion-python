# Definir una lista de números
numeros = [4, 2, 7, 4, 9, 4, 1, 4]

# Pedir un número al usuario
numero = int(input("Introduce un número: "))

# Contar cuántas veces aparece el número en la lista
contador = numeros.count(numero)

# Mostrar el resultado
print(f"El número {numero} aparece {contador} veces en la lista.")