#Pedir una opción por pantalla y decir por pantalla si es “opción 1” , “opción 2”, “opción 3 o 4”, “ninguna de las anteriores”. Utilizar un match case
opcion = int(input("Opción: "))

match opcion:
    case 1:
        print("Opción 1")
    case 2:
        print("Opción 2")
    case 3 | 4:
        print("Opción 3 o 4")
    case _:
        print("ninguna de las anteriores")
