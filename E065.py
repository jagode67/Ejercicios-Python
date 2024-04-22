'''E065
Tenemos la siguiente lista: nombres = [“Carlos", “Lara", "María José", “María", “Ana"].
Sacar por pantalla el nombre más largo y el más corto.


'''
nombres = ["Carlos", "Lara", "María José", "María", "Ana"]

# Inicializar variables
nombre_mas_largo = nombres[0]
nombre_mas_corto = nombres[0]

# Recorrer la lista
for nombre in nombres:
  # Comparar longitudes y actualizar variables
  if len(nombre) > len(nombre_mas_largo):
    nombre_mas_largo = nombre
  elif len(nombre) < len(nombre_mas_corto):
    nombre_mas_corto = nombre

# Imprimir resultados
print(f"Nombre más largo: {nombre_mas_largo}")
print(f"Nombre más corto: {nombre_mas_corto}")

