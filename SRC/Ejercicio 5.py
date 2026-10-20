# calcular la suma de los numeros pares del 1 al 100
Suma_de_pares= 0
for numerospares in range(1, 100):
    if numerospares % 2 == 0:
        Suma_de_pares += numerospares
print (f" La suma de numeros pares es de: {Suma_de_pares}")

