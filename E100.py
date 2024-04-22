'''E100
Crear una función en Python que reciba una lista de palabras y 
devuelva un diccionario con la cantidad de veces que aparece 
la palabra en la lista. La carga de la lista de palabras se 
hace por teclado hasta que se pulsa la tecla INTRO

'''
def contarPalabras(palabras):
  frecuencias = {}
  for palabra in palabras:
    if palabra in frecuencias:
      frecuencias[palabra] += 1
    else:
      frecuencias[palabra] = 1
  return frecuencias
# Obtener la lista de palabras del usuario
palabras = []
while True:
  palabra = input("Introduce una palabra (o pulsa INTRO para terminar): ")
  if palabra == "":
    break
  palabras.append(palabra)
# Contar la frecuencia de las palabras
frecuencias = contarPalabras(palabras)
# Mostrar la frecuencia de las palabras
for palabra, frecuencia in frecuencias.items():
  print(f"Palabra: {palabra}, Frecuencia: {frecuencia}")
