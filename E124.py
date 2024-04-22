'''E124
Crear un error personalizado (miError).
Se debe lanzar este error cuando el valor numérico introducido sea menor de 0

'''

class miError(Exception):
    def __init__(self,mensaje,codigo):
        super().__init__(mensaje)
        self.codigo=codigo


correcto = False
while not correcto:
    try:
        a= int(input("Introduce valor mayor de 0: "))
        if a<0:
            raise miError("ERROR: debe mayor de 0",1001)

    except miError as e:
        print (e, e.codigo)

    except ValueError as e:
        print("ERROR: Valor no numérico. Vuelve a intentarlo")
    else:
        correcto =True



