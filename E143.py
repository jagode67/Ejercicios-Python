'''E143
Mostrar el contenido del archivo “numeros.txt”. Si el archivo no existe, el programa debe decir “Archivo no encontrado”.

'''

try:
    with open("numeros.txt","r",encoding="utf-8") as a:
        p=a.read()
        print (p)
except FileNotFoundError as a:
    print("Archivo no encontrado")

