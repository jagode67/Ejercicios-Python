'''E125
Solicitar dos números por pantalla y dar el resultado de su división.
Los números no deben de ser iguales. Controlar los errores con try de que deben ser números,
la división entre cero y que los números no deben ser iguales.
Repetir la solicitud de datos hasta que todo esté correcto

'''
class errorIguales(Exception):

    def __init__(self, mensaje):
        self.message = mensaje

resultado = None
while True:
    try:
        a = int(input('Primer número: '))
        b = int(input('Segundo número: '))
        if a == b:
            raise errorIguales('números indénticos')
        resultado = a/b
        break
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError - Ocurrió un error: {e} , {type(e)}")

    except TypeError as e:
        print(f"TypeError - Ocurrió un error: {e} , {type(e)}")

    except Exception as e:
        print(f"Exception - Ocurrió un error: {e} , {type(e)}")



print(f'Resultado: {resultado}')





