'''E102
Crear dos funciones, una que introduzca una lista de números hasta que se pulse INTRO y
otra que devuelva la media de los números de la lista

# Obtener la lista de números del usuario
numeros = leer_numeros()
# Calcular el promedio de la lista
promedio = calcular_promedio(numeros)
# Mostrar el promedio
if promedio is None:
  print("No se ha introducido ningún número.")
else:
  print(f"El promedio de la lista es: {promedio}")

'''

def leer_numeros():
  numeros = []
  while True:
    numero = input("Introduce un número (o pulsa INTRO para terminar): ")
    if numero == "":
      break
    numeros.append(float(numero))
  return numeros
def calcular_promedio(numeros):
  if len(numeros) == 0:
    return None
  else:
    suma = sum(numeros)
    promedio = suma / len(numeros)
    return promedio

# Obtener la lista de números del usuario
numeros = leer_numeros()
# Calcular el promedio de la lista
promedio = calcular_promedio(numeros)
# Mostrar el promedio
if promedio is None:
  print("No se ha introducido ningún número.")
else:
  print(f"El promedio de la lista es: {promedio}")


