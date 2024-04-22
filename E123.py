'''E123
Pedir dos números correctos por pantalla y sacar el resultado de su división. Controlar todos los errores.
Introduce valor A: s
ERROR: Valor no numérico. Vuelve a intentarlo
Introduce valor A: 1
Introduce valor B: 0
ERROR: El divisor es 0
Introduce valor A: 4
Introduce valor B: 2
División:  2.0

'''
correcto = False
while not correcto:
    try:
        a= int(input("Introduce valor A: "))
        b = int(input("Introduce valor B: "))
        print ("División: " , a/b)

    except ZeroDivisionError as e:
        print ("ERROR: El divisor es 0")

    except ValueError as e:
        print("ERROR: Valor no numérico. Vuelve a intentarlo")
    else:
        correcto =True



