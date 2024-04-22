'''E133
Leer los tres primeros caracteres del archivo a.txt con with. Si el archivo no existe, el programa debe decir “Archivo no encontrado”

'''

try:
    with open("a.txt","r",encoding="utf-8") as a:
        t=a.read(3)
        print(t)
except FileNotFoundError as a:
    print("Archivo no encontrado")




