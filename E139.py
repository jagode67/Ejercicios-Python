'''E139
Decir cuantas vocales están grabadas en el archivo “palabras.txt”. Si el archivo no existe, el programa debe decir “Archivo no encontrado”

'''
vocales=["a","e","i","o","u"]
c=0
try:
    with open("palabras.txt","r",encoding="utf-8") as a:
        p=a.read()
        for ele in p:
            if ele.lower() in vocales:
                c+=1
        print (f"Hay: {c} vocales")
except FileNotFoundError as a:
    print("Archivo no encontrado")

