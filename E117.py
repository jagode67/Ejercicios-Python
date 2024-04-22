'''E117
Crear la clase Persona con los atributos nombre y edad.
Tener una variable  contador que cuente la cantidad de Personas creadas
a=Persona("Javi",56)
print (Persona.contador)
a=Persona("Carlos",23)
print (Persona.contador)

'''
class Persona:
    contador=0
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        Persona.contador+=1

a=Persona("Javi",56)
print (Persona.contador)
a=Persona("Carlos",23)
print (Persona.contador)
