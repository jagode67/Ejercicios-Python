'''E095
Definir una función listar() que reciba una cantidad de parámetros variable y los muestre por pantalla.
'''

def listar(*args):
    for arg in args:
        print(arg)

listar(1,2,3)
listar("uno","dos","tres","cuatro")
