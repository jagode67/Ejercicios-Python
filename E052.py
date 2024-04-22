'''E052
Crear una lista con los valores 1,2,3,4,5. Pedir un número por pantalla y si está en la lista decir “Está en la lista”
en caso contrario “No está en la lista”
'''
lista=[1,2,3,4,5]
ele=int(input("Dime un número: "))
if ele in lista:
    print("Está en la lista")
else:
    print("No está en la lista")

