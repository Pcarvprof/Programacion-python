# Inicializar el contador
contador = 0

for i in range(5):
    numero = float(input(f"Introduce el número {i + 1}: "))
    if numero > 10:
        contador += 1

print(f"Has introducido {contador} números mayores que 10.")