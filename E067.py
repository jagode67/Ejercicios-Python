'''E067
Tenemos la siguiente lista: nombres = [“Carlos", “Lara", "María José", “María", “Ana"].
Solicitar por pantalla un nombre y si existe en la lista, borrarlo.
A continuación, volver a mostrar la lista.

'''
nombres = ["Carlos", "Lara", "María José", "María", "Ana"]

# Solicitar nombre al usuario
nombre_a_borrar = input("Introduce un nombre a borrar: ")

# Buscar el nombre en la lista
if nombre_a_borrar in nombres:
  # Eliminar el nombre de la lista
  nombres.remove(nombre_a_borrar)
  print(f"El nombre '{nombre_a_borrar}' ha sido borrado.")
else:
  print(f"El nombre '{nombre_a_borrar}' no está en la lista.")

# Mostrar la lista actualizada
print("Lista actualizada:", nombres)
