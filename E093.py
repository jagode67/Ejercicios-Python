'''E093
Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Crear la lista por teclado hasta que se introduzca 0.

'''

def sum(lista):
    suma=0
    for i in lista:
        suma+=i
    return suma

def multip (lista):
    mult=1
    for i in lista:
        mult*=i
    return mult

numeros=[]
while True:
    x=int(input("Número:"))
    if x==0:
        break
    else:
        numeros.append(x)

print(sum(numeros))
print(multip(numeros))
