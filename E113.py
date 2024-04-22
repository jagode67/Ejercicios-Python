'''E113
Crear la clase Persona con los atributos nombre y edad y con el método __str__ para mostrar su contenido. Crear la clase Empleado con el método __str__ que muestre su contenido utilizando el __str__ de su padre
p=Persona('Javi',56)
print (p)
e = Empleado('Juan', 28, 5000)
print (e)

Nombre: Javi Edad: 56
Nombre: Juan Edad: 28 Nombre: Juan Edad: 28

'''


class Persona:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad
  def __str__(self):
    return f"Nombre: {self.nombre} Edad: {self.edad}"


class Empleado(Persona):
  def __init__(self, nombre, edad, sueldo):
    super().__init__(nombre, edad)
    self.sueldo = sueldo
  def __str__(self):
    return f"{super().__str__()} Nombre: {self.nombre} Edad: {self.edad}"

p=Persona('Javi',56)
print (p)
e = Empleado('Juan', 28, 5000)
print (e)
