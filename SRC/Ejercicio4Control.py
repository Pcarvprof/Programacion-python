# Inicializar el contador
contador = 0

# Usar un bucle for para pedir 5 números
for i in range(5):
    numero = float(input(f"Introduce el número {i + 1}: "))
    if numero > 10:
        contador += 1

# Mostrar cuántos números fueron mayores que 10
print(f"Has introducido {contador} números mayores que 10.")