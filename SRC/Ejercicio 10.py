# elegir operacion matematica


import math
import time



while True:
    print("Elige una operación matemática:")
    print("Pulsa 1 para suma")
    print("Pulsa 2 para resta")
    print("Pulsa 3 para multiplicación")
    print("Pulsa 4 para división")
    print("Pulsa 5 para potencia")
    print("Pulsa 6 para raíz cuadrada")
    print("Pulsa 7 para logaritmo")
    print("Pulsa 8 para ecuación de primer grado")
    print("Pulsa 9 para sistema de ecuaciones")
    print("Pulsa 10 para volver al menú")
    print("Pulsa 11 para apagar la calculadora")

    Operacion_matematica = input("Elige una opción: ")

    if Operacion_matematica == "11":
        print("Apagando la calculadora. ¡Hasta pronto!")
        break

    elif Operacion_matematica == "10":
        continue

    elif Operacion_matematica not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print("Operación no válida. Elige una opción del 1 al 11.")

    elif Operacion_matematica == "1":
        Numero_1 = float(input("Introduce el primer número: "))
        Numero_2 = float(input("Introduce el segundo número: "))
        resultado = Numero_1 + Numero_2
        print(f"El resultado de la suma es: {resultado}")

    elif Operacion_matematica == "2":
        Numero_1 = float(input("Introduce el primer número: "))
        Numero_2 = float(input("Introduce el segundo número: "))
        resultado = Numero_1 - Numero_2
        print(f"El resultado de la resta es: {resultado}")

    elif Operacion_matematica == "3":
        Numero_1 = float(input("Introduce el primer número: "))
        Numero_2 = float(input("Introduce el segundo número: "))
        resultado = Numero_1 * Numero_2
        print(f"El resultado de la multiplicación es: {resultado}")

    elif Operacion_matematica == "4":
        Numero_1 = float(input("Introduce el primer número: "))
        Numero_2 = float(input("Introduce el segundo número: "))

        if Numero_2 == 0:
            print("Error: No se puede dividir entre cero.")
        else:
            resultado = Numero_1 / Numero_2
            print(f"El resultado de la división es: {resultado}")

    elif Operacion_matematica == "5":
        Numero_1 = float(input("Introduce el primer número: "))
        Numero_2 = float(input("Introduce el segundo número: "))
        resultado = Numero_1 ** Numero_2
        print(f"El resultado de la potencia es: {resultado}")

    elif Operacion_matematica == "6":
        Numero_1 = float(input("Introduce el número: "))

        if Numero_1 < 0:
            print("Error: No se puede calcular la raíz cuadrada de un número negativo.")
        else:
            resultado = math.sqrt(Numero_1)
            print(f"El resultado de la raíz cuadrada es: {resultado}")

    elif Operacion_matematica == "7":
        Numero_1 = float(input("Introduce el número: "))

        if Numero_1 <= 0:
            print("Error: El logaritmo necesita un número mayor que cero.")
        else:
            resultado = math.log(Numero_1)
            print(f"El resultado del logaritmo es: {resultado}")

    elif Operacion_matematica == "8":
        a = float(input("Introduce el valor de a: "))
        b = float(input("Introduce el valor de b: "))

        if a == 0:
            if b == 0:
                print("La ecuación tiene infinitas soluciones.")
            else:
                print("La ecuación no tiene solución.")
        else:
            x = -b / a
            print(f"La solución de la ecuación es: x = {x}")

    elif Operacion_matematica == "9":
        print("Sistema de ecuaciones:")
        print("a1*x + b1*y = c1")
        print("a2*x + b2*y = c2")

        a1 = float(input("Introduce el valor de a1: "))
        b1 = float(input("Introduce el valor de b1: "))
        c1 = float(input("Introduce el valor de c1: "))

        a2 = float(input("Introduce el valor de a2: "))
        b2 = float(input("Introduce el valor de b2: "))
        c2 = float(input("Introduce el valor de c2: "))

        determinante = a1 * b2 - a2 * b1

        if determinante == 0:
            print("El sistema no tiene una solución única.")
        else:
            x = (c1 * b2 - c2 * b1) / determinante
            y = (a1 * c2 - a2 * c1) / determinante
            print(f"La solución del sistema es: x = {x}, y = {y}")

    print("Puedes realizar otra operación.")
    time.sleep(5)