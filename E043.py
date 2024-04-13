# Escribir un programa que imprima una tabla de multiplicar del 1 al 10.

for numero in range(1, 11):
  print(f"Tabla de multiplicar del {numero}")
  for multiplicador in range(1, 11):
    print(f"{numero} x {multiplicador} = {numero * multiplicador}")
