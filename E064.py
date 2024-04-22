'''E064
Crear una lista con los valores “uno”,”dos”,”tres”,
crear otra lista con los datos de la primera ordenada de forma inversa
y mostrar todos los elementos de la ordenada a través de un for


'''
lista=["uno","dos","tres"]
lista2=sorted(lista,reverse=True)
for ele in lista2:
    print (ele)
