'''E074
Solicitar nombres por pantalla hasta que el usuario pulse la tecla INTRO y mostrarla sin valores repetidos. Utilizar un set

'''
nombres = set()

while True:
  nombre = input("Introduce un nombre (o pulsa INTRO para terminar): ")
  if nombre == "":
    break
  nombres.add(nombre)

print("Lista de nombres sin valores repetidos:", nombres)

