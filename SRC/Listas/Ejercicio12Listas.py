# Definir una lista de palabras
palabras = ["Hola", "mundo", "esto", "es", "Python"]

cadena_concatenada = ""
for palabra in palabras:
    cadena_concatenada += palabra + " "

cadena_concatenada = cadena_concatenada.strip()

print(f"Cadena resultante: {cadena_concatenada}")