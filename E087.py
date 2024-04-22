'''E087
Crear la función multiplica que reciba dos parámetros y devuelva el resultado de la multiplicación de ambos parámetros. Si recibe un solo parámetro, debe devolver el cuadrado de este.
print (multiplica(3))
print (multiplica(12,3))
'''

def multiplica(a,b="vacio"):
    if b=="vacio":
        return a**2
    else:
        return a*b


print (multiplica(3))
print (multiplica(12,3))

