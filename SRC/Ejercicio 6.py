# encontrar el mayor numero de tres numeros
Numero_1 = 0
Numero_2 = 0
Numero_3 = 0
Numero_1 = float(input("Introduce el primer número: "))
Numero_2 = float(input("Introduce el segundo número: "))   
Numero_3 = float(input("Introduce el tercer número: "))
if Numero_1 > Numero_2 and Numero_1 > Numero_3:
    print(f"El mayor número es: {Numero_1}")
elif Numero_2 > Numero_1 and Numero_2 > Numero_3:
    print(f"El mayor número es: {Numero_2}")
else:
    print(f"El mayor número es: {Numero_3}")