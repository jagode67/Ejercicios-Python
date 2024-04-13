#Pedir un número por pantalla y mostrar con un guion en medio todos los números desde el cero hasta ese valor introducido. Utilizar un while
num=int(input("Introducir un número: "))
a=0
while a<=num:
    print (a,end="-")
    a+=1