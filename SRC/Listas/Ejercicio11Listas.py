# Definir una lista de caracteres
caracteres = ['a', 'b', 'c', 'e', 'i', 'o', 'u', 'x', 'z']

# Definir las vocales
vocales = ['a', 'e', 'i', 'o', 'u']

# Inicializar el contador de vocales
contador_vocales = 0

# Recorrer la lista de caracteres y contar las vocales
for caracter in caracteres:
    if caracter in vocales:
        contador_vocales += 1

# Mostrar el resultado
print(f"Hay {contador_vocales} vocales en la lista.")