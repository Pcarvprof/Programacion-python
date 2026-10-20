# contar cuantos numeros son mayoes que 10
Contador_de_numeros= 0

for i in range(5):
    numero = float(input(f"Introduce el número {i + 1}: "))
    if numero > 10:
        Contador_de_numeros += 1
print(f"La cantidad de números mayores que 10 es: {Contador_de_numeros}")