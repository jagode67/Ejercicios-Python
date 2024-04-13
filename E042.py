# Escribir un programa que pida al usuario una cadena de caracteres y luego imprima la cadena al revés.
# len(cadena): cantidad de caracteres de una cadena
cadena = input("Introduce una cadena de caracteres: ")

for i in range(len(cadena)-1, -1, -1):
  print(cadena[i])
