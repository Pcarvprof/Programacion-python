#suma de digitos de un numero
Numero = int(input("Introduce un número: "))
suma_de_digitos=0
for digito in (str(Numero)):
    suma_de_digitos += int(digito)
print(f"La suma de los dígitos del número {Numero} es: {suma_de_digitos}")