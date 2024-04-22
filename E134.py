'''E134
Leer la primera línea del archivo c.txt con with. Si el archivo no existe, el programa debe decir “Archivo no encontrado”

'''

try:
    with open("c.txt","r",encoding="utf-8") as a:
        t=a.readline()
        print(t)
except FileNotFoundError as a:
    print("Archivo no encontrado")




