numero = int(input("Introduce un número entero: "))

# Inicializar el resultado del factorial
factorial = 1

# Usar un bucle while para calcular el factorial
while numero > 0:
    factorial *= numero
    numero -= 1

# Mostrar el resultado
print(f"El factorial es: {factorial}")