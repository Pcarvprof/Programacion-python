opcion = 0

while opcion != 4:
    # Mostrar el menú
    print("Menú de operaciones:")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Salir")
    
    opcion = int(input("Elige una opción (1-4): "))
    
    if opcion == 1:
        numero1 = float(input("Introduce el primer número: "))
        numero2 = float(input("Introduce el segundo número: "))
        print(f"La suma es: {numero1 + numero2}")
    
    elif opcion == 2:
        numero1 = float(input("Introduce el primer número: "))
        numero2 = float(input("Introduce el segundo número: "))
        print(f"La resta es: {numero1 - numero2}")
    
    elif opcion == 3:
        numero1 = float(input("Introduce el primer número: "))
        numero2 = float(input("Introduce el segundo número: "))
        print(f"La multiplicación es: {numero1 * numero2}")
    
    elif opcion == 4:
        print("Saliendo del programa...")
    
    else:
        print("Opción no válida. Intenta de nuevo.")