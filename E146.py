'''E146
Reescribir el archivo “números.txt” quitando todos los números repetidos.
Si el archivo no existe, el programa debe decir “Archivo no encontrado”.

'''
t=0
try:
    with open("numeros.txt","r",encoding="utf-8") as a:
        c=a.readlines()
        s=set(c)
    with open("numeros.txt","w",encoding="utf-8") as a:
        for ele in s:
            a.write(ele)
except FileNotFoundError as a:
    print("Archivo no encontrado")


