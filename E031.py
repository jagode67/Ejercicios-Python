#Pedir un número por pantalla y mostrar con un asterisco en medio todos los números desde el número introducido hasta el cero. Utilizar un while
num=int(input("Introducir un número: "))
a=num
while a>=0:
    print (a,end="*")
    a-=1