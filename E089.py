'''E089
Definir una función maxi() que tome como argumento dos números y devuelva el mayor de ellos.
(Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un
muy buen ejercicio.

print(max(10,10))
maxi(10,10)
maxi(10,11)
maxi(30,10)

'''

def maxi(n1,n2):
    if n1<n2:
        print (n2)
    elif n2<n1:
        print (n1)
    else:
        print ("Son iguales")

print(max(10,10))
maxi(10,10)
maxi(10,11)
maxi(30,10)


