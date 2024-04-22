'''E082
Solicitar palabras por pantalla hasta que se deje pulse INTRO sin ninguna palabra y
mostrar utilizando un diccionario, la frecuencia de aparición de esas palabras.

'''

frecuencias = {}
while True:
    palabra = input("Introduce una palabra (o pulsa INTRO para terminar): ")
    if palabra == "":
        break
    if palabra in frecuencias:
        frecuencias[palabra] += 1
    else:
        frecuencias[palabra] = 1
# Mostrar la frecuencia de las palabras
for palabra, frecuencia in frecuencias.items():
    print(f"Palabra: {palabra}, Frecuencia: {frecuencia}")

