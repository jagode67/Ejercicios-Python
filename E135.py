'''E135
Leer el archivo c.txt con with e introduce su contenido en una lista en donde cada línea sea un elemento de la lista.
Muestra la lista. Si el archivo no existe, el programa debe decir “Archivo no encontrado”

'''

try:
    with open("c.txt","r",encoding="utf-8") as a:
        t=a.readlines()
        print(t)
except FileNotFoundError as a:
    print("Archivo no encontrado")




