'''E122
Pedir un número por pantalla y no dejar de pedirlo hasta que no se introduzca un número correcto.
Introduce valor: s
Valor no numérico. Vuelve a intentarlo
Introduce valor: 2

'''
correcto = False
while not correcto:
    try:
        valor=int(input("Introduce valor: "))
    except ValueError as e:
        print("Valor no numérico. Vuelve a intentarlo")
    else:
        correcto =True



