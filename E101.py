'''E101
Crear una función que reciba un texto y devuelva un diccionario con la
frecuencia de aparición de las palabras que tiene el texto.

'''

def contarPalabras(texto):
  # Convertir el texto a minúsculas y dividirlo en palabras
  palabras = texto.lower().split()
  # Contar la frecuencia de las palabras
  frecuencias = {}
  for palabra in palabras:
    if palabra in frecuencias:
      frecuencias[palabra] += 1
    else:
      frecuencias[palabra] = 1
  return frecuencias


# Ejemplo de uso
texto = "Este es un ejemplo de un texto para contar la frecuencia de las palabras."
frecuencias = contarPalabras(texto)
# Mostrar la frecuencia de las palabras
for palabra, frecuencia in frecuencias.items():
  print(f"Palabra: {palabra}, Fec: {frecuencia}")