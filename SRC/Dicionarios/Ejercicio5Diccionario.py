# Pedir una palabra al usuario
palabra = input("Introduce una palabra: ")

frecuencia_letras = {}

for letra in palabra:
    if letra in frecuencia_letras:
        frecuencia_letras[letra] += 1
    else:
        frecuencia_letras[letra] = 1

print("Frecuencia de letras:", frecuencia_letras)