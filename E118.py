'''E118
Crear la clase Persona con los atributos nombre y edad. Tener una variable  contador que cuente la cantidad de Personas creadas. Crear un método estático numero() que muestre la cantidad de personas.
a=Persona("Javi",56)
Persona.numero()
a=Persona("Carlos",23)
Persona.numero()

Cantidad de personas: 1
Cantidad de personas: 2

'''
class Persona:
    contador=0

    @staticmethod
    def numero():
        print("Cantidad de personas:",Persona.contador)

    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        Persona.contador+=1

a=Persona("Javi",56)
Persona.numero()
a=Persona("Carlos",23)
Persona.numero()

