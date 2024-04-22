'''E107
Crear la clase Persona con los atributos nombre y edad. Crear un método mostrarDetalle() que imprima los valores del objeto
p=Persona("Javi",56)
p.mostrarDetalle()

Nombre: Javi - Edad: 56

'''


class Persona:
  def __init__(self,nombre,edad):
    self.nombre=nombre
    self.edad=edad

  def mostrarDetalle(self):
    print(f"Nombre: {self.nombre} - Edad: {self.edad}")

p=Persona("Javi",56)
p.mostrarDetalle()
