'''E150
Leer el archivo “poblacion.txt” y reescribirlo de manera que, si hay dos provincias iguales,
sumar los habitantes de estos registros y grabar la suma.

'''
with open("poblacion.txt", "r") as archivo_lectura:
  lineas = archivo_lectura.readlines()

datos_poblacion = {}
for linea in lineas:
  provincia, habitantes = linea.strip().split(",")
  habitantes = int(habitantes)
  datos_poblacion.setdefault(provincia, 0)  # Inicializar con 0 si no existe
  datos_poblacion[provincia] += habitantes  # Sumar habitantes

with open("poblacion.txt", "w") as archivo_escritura:
  for provincia, habitantes in datos_poblacion.items():
    linea = f"{provincia},{habitantes}\n"
    archivo_escritura.write(linea)

