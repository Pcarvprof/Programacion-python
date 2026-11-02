# Usar un bucle for para recorrer los números del 1 al 10
for numero in range(1, 11):
    if numero % 2 == 0:
        continue  # Omitir el resto del bucle si el número es par
    print(numero)