'''E140
Mostrar el contenido del archivo “palabras.txt”. Si el archivo no existe, el programa debe decir “Archivo no encontrado”

'''
vocales=["a","e","i","o","u"]
c=0
try:
    with open("palabras.txt","r",encoding="utf-8") as a:
        p=a.read()
        print (p)
except FileNotFoundError as a:
    print("Archivo no encontrado")

