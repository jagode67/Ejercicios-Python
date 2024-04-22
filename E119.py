'''E119
Crear la clase Persona con los atributos id, nombre y edad. El nombre y la edad se reciben por parámetro al crear la clase y el atributo id es una secuencia que tendrá el valor 1 para el primer objeto, 2 para el segundo…
persona1 = Persona('Javi', 28)
print(persona1)
persona2 = Persona('Lara', 30)
print(persona2)
persona3 = Persona('Carlos', 25)
print(persona3)
Persona.generar_siguiente_valor()
persona4 = Persona('María', 35)
print(persona4)
print(f'Valor contador personas: {Persona.contador_personas}')

Persona [1 Javi 28]
Persona [2 Lara 30]
Persona [3 Carlos 25]
Persona [5 María 35]
Valor contador personas: 5

'''
class Persona:
    contador_personas = 0

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas += 1
        return cls.contador_personas

    def __init__(self, nombre, edad):
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona [{self.id_persona} {self.nombre} {self.edad}]'

persona1 = Persona('Javi', 28)
print(persona1)
persona2 = Persona('Lara', 30)
print(persona2)
persona3 = Persona('Carlos', 25)
print(persona3)
Persona.generar_siguiente_valor()
persona4 = Persona('María', 35)
print(persona4)
print(f'Valor contador personas: {Persona.contador_personas}')


