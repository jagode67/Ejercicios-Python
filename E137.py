'''E137
Decir cuantas palabras están grabadas en el archivo “palabras.txt”. Si el archivo no existe, el programa debe decir “Archivo no encontrado”

'''
try:
    with open("palabras.txt","r",encoding="utf-8") as a:
        p=a.readlines()
        print (len(p))
except FileNotFoundError as a:
    print("Archivo no encontrado")

