'''E091
Definir la función largo_cadena() que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.
print(largo_cadena("periquito"))

'''

def largo_cadena(lista):
    cont=0
    for i in lista:
        cont+=1
    return cont

print(largo_cadena("periquito"))


