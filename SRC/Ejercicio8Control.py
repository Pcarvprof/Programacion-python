# Solicitar un número entero al usuario
numero = input("Introduce un número entero: ")

# Inicializar la suma
suma = 0

# Recorrer los dígitos y sumarlos
for digito in numero:
    suma += int(digito)

# Mostrar la suma de los dígitos
print(f"La suma de los dígitos es: {suma}")