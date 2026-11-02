# Definir dos listas
claves = ["nombre", "edad", "ciudad"]
valores = ["Ana", 28, "Barcelona"]

diccionario = {}

for i in range(len(claves)):
    diccionario[claves[i]] = valores[i]

print("Diccionario creado:", diccionario)