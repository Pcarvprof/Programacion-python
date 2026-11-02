# Usar un bucle for para recorrer los números del 51 al 100
for numero in range(51, 101):
    if numero % 7 != 0:
        continue  # Saltar si el número no es múltiplo de 7
    print(f"El primer múltiplo de 7 mayor que 50 es: {numero}")
    break  # Detener el bucle al encontrar el primer múltiplo de 7