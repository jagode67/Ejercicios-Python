'''E148
Pedir por pantalla una provincia y su cantidad de habitantes y grabar un archivo llamado “poblacion.txt”
que por cada línea tenga la provincia y cantidad de habitantes separado por coma.
Dejar de pedir provincias cuando se deje la provincia en blanco

'''
with open("poblacion.txt", "w") as a:
  while True:
    provincia = input("Provincia (en blanco para terminar): ")
    if not provincia:
      break

    habitantes = input("Cantidad de habitantes: ")
    try:
      habitantes = int(habitantes)
    except ValueError:
      print("Error: La cantidad de habitantes debe ser un número entero.")

    linea = f"{provincia},{habitantes}\n"
    a.write(linea)
