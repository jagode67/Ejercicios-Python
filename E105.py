'''E105
Crear la clase Persona con los atributos nombre y edad.
Cuando se crea el objeto se carga con la información “Vacío”.
Probar con el siguiente código.
p=Persona()
print(p.nombre)
print(p.edad)
p.nombre="Javi"
p.edad=56
print(p.nombre)
print(p.edad)

'''


class Persona:
  def __init__(self):
    self.nombre="Vacío"
    self.edad=0

p=Persona()
print(p.nombre)
print(p.edad)
p.nombre="Javi"
p.edad=56
print(p.nombre)
print(p.edad)

