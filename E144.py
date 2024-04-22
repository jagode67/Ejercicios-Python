'''E144
Mostrar la suma de todos los números del archivo “numeros.txt”. Si el archivo no existe, el programa debe decir “Archivo no encontrado”.

'''
t=0
try:
    with open("numeros.txt","r",encoding="utf-8") as a:
        for ele in a:
            t+=int(ele)
        print (f"Total: {t}")
except FileNotFoundError as a:
    print("Archivo no encontrado")


