numero = int(input("Introduce un número entero: "))
factorial = 1

while numero > 0:
    factorial *= numero
    numero -= 1

print(f"El factorial es: {factorial}")