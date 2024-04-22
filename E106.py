'''E106
Crear la clase Persona con los atributos nombre y edad. En el constructor, admitir estos dos valores.
p=Persona("Javi",56)
print(p.nombre)
print(p.edad)

'''


class Persona:
  def __init__(self,nombre,edad):
    self.nombre=nombre
    self.edad=edad

p=Persona("Javi",56)
print(p.nombre)
print(p.edad)
