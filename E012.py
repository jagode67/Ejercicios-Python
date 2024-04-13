#Pedir un número por pantalla y decir si está entre el 5 y el 10 (ambos inclusive). Utilizar el operador ‘and’
valor=int(input("Introduce un valor: "))
if (valor>=5) and (valor<=10):
    print("Está dentro del rango")
else:
    print("Está fuera del rango")
