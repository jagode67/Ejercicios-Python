'''E147
Reescribir el archivo “números.txt” ordenando los números de menor a mayor.
Si el archivo no existe, el programa debe decir “Archivo no encontrado”.

'''
t=0
def orden(v):
    return int(v)

try:
    with open("numeros.txt","r",encoding="utf-8") as a:
        c=a.readlines()
        c.sort(key=orden)
    with open("numeros.txt","w",encoding="utf-8") as a:
        for ele in c:
            a.write(ele)
except FileNotFoundError as a:
    print("Archivo no encontrado")


