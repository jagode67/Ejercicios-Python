'''E138
Decir cual es la palabra mas larga y su longitud del archivo “palabras.txt”. Si el archivo no existe, el programa debe decir “Archivo no encontrado”

'''
lMax=0
pMax=""
try:
    with open("palabras.txt","r",encoding="utf-8") as a:
        p=a.readlines()
        for ele in p:
            if lMax < len(ele):
                lMax=len(ele)
                pMax=ele
        print (f"La palabra mas larga es: {pMax} con {lMax-1} caracteres")
except FileNotFoundError as a:
    print("Archivo no encontrado")

