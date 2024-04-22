'''E066

Solicitar por pantalla un conjunto de números hasta que se introduzca un 0 y
mostrarlo por pantalla en orden descendente. Utilizar listas



'''
numeros = []

# Solicitar números al usuario
while True:
  numero = int(input("Introduce un número (o 0 para terminar): "))
  if numero == 0:
    break
  numeros.append(numero)

# Ordenar la lista en orden descendente
numeros.sort(reverse=True)

# Mostrar la lista
print("Números en orden descendente:", numeros)
