# Escribir un programa que imprima la suma de los números pares del 1 al 100.
total=0
for numero in range(1, 101):
  # Si el número es par, sumarlo a la variable total
  if numero % 2 == 0:
    total += numero

# Imprimir la suma total
print("La suma de los números pares del 1 al 100 es", total)