'''E145
Mostrar la media de todos los números del archivo “numeros.txt”. Si el archivo no existe, el programa debe decir “Archivo no encontrado”.

'''
t=0
try:
    with open("numeros.txt","r",encoding="utf-8") as a:
        c=a.readlines()
        for ele in c:
            t+=int(ele)
        print (f"Total: {t/len(c)}")
except FileNotFoundError as a:
    print("Archivo no encontrado")


