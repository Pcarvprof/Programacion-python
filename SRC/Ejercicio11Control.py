# Definir el número secreto
numero_secreto = 7

# Inicializar el número de intentos
intentos = 0

# Usar un bucle para permitir hasta 5 intentos
while intentos < 5:
    numero = int(input("Adivina el número (entre 1 y 10): "))
    
    if numero == numero_secreto:
        print("¡Felicidades! Has adivinado el número.")
        break  # Salir del bucle si el número es correcto
    else:
        print("Número incorrecto. Inténtalo de nuevo.")
    
    intentos += 1

if intentos == 5 and numero != numero_secreto:
    print("Lo siento, has agotado todos los intentos.")