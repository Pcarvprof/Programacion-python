#contar los multiplos de 3 entre 2 numeros
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
contador = 0
for i in range(numero1, numero2 + 1):
    if i % 3 == 0:
        contador += 1
print("El número de múltiplos de 3 entre", numero1, "y", numero2, "es:", contador)