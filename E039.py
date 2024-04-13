# Escribir un programa que pida al usuario dos números enteros positivos y muestre por pantalla la tabla de multiplicar del primer número hasta el segundo número.
numero_inicial = int(input("Introduce un número entero positivo (inicio): "))
numero_final = int(input("Introduce un número entero positivo (fin): "))

while numero_inicial <= numero_final:
  print("Tabla de multiplicar del", numero_inicial)

  for multiplicador in range(1, 11):
    print(f"{numero_inicial} x {multiplicador} = {numero_inicial * multiplicador}")

  numero_inicial += 1