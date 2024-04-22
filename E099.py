'''E099
Crear una función mostarElementos() y pasar como parámetro una lista. La función tiene que mostrar los elementos de la lista.
mostrarElementos([1,2,3,4])
mostrarElementos(["uno","dos","tres"])

'''

def mostrarElementos(lista):
    for ele in lista:
        print(f"Elemento: {ele}")


mostrarElementos([1,2,3,4])
mostrarElementos(["uno","dos","tres"])