'''E148
Pedir por pantalla una provincia y su cantidad de habitantes y grabar un archivo llamado “poblacion.txt”
que por cada línea tenga la provincia y cantidad de habitantes separado por coma.
Dejar de pedir provincias cuando se deje la provincia en blanco

'''
datos_poblacion = {}
with open("poblacion.txt", "r") as a:
  for linea in a:
    provincia, habitantes = linea.strip().split(",")
    habitantes = int(habitantes)
    datos_poblacion.setdefault(provincia, 0)
    datos_poblacion[provincia] += habitantes

# Encontrar la provincia con más habitantes
provincia_mas_poblada = None
maxima_poblacion = 0
for provincia, poblacion in datos_poblacion.items():
  if poblacion > maxima_poblacion:
    provincia_mas_poblada = provincia
    maxima_poblacion = poblacion
  elif poblacion == maxima_poblacion:
    provincia_mas_poblada = "Empate"

# Devolver el resultado
if provincia_mas_poblada:
  print( f"La provincia con más habitantes es {provincia_mas_poblada} con {maxima_poblacion} habitantes.")
else:
  print ("No hay datos de población en el archivo.")


