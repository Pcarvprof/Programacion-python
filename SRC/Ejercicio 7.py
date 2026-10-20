Numero_1 = float(input("Introduce el primer número: "))
Numero_2 = float(input("Introduce el segundo número: "))

Multiplos_de_3 = 0

if Numero_1 > Numero_2:
    Numero_1, Numero_2 = Numero_2, Numero_1

for multiplos in range(int(Numero_1), int(Numero_2) + 1):
    if multiplos % 3 == 0:
        Multiplos_de_3 += 1

print(f"El número de múltiplos de 3 entre {Numero_1} y {Numero_2} es: {Multiplos_de_3}")
