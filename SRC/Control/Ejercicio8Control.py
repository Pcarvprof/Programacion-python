# Solicitar un número entero al usuario
numero = input("Introduce un número entero: ")
suma = 0

for digito in numero:
    suma += int(digito)

print(f"La suma de los dígitos es: {suma}")