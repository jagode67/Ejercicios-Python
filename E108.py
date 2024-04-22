'''E108
Crear la clase Persona con los atributos nombre y edad. Cuando se imprima el objeto se debe ver su contenido.
p=Persona("Javi",56)
print(p)

'''


class Persona:
  def __init__(self,nombre,edad):
    self.nombre=nombre
    self.edad=edad

  def __str__(self):
    return f"Nombre: {self.nombre} - Edad: {self.edad}"

p=Persona("Javi",56)
print(p)
