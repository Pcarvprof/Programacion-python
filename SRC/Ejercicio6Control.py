#encontrar el mayor de 3 numeros
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
numero3 = float(input("Introduce el tercer número: "))
if numero1 >= numero2 and numero1 >= numero3:
    print("El mayor es:", numero1)
elif numero2 >= numero1 and numero2 >= numero3:
    print("El mayor es:", numero2)
else:
    print("El mayor es:", numero3)
