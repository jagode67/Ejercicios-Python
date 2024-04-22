'''E115
Definir una clase Color con el atributo color y el método __str__. Definir unaclase Figura con el atributo lado y el método __str__. Definir la clase Cuadrado con el atributo textura y que herede de Color y Figura. Debe tener el método __str__
c=Color("verde")
print (c)

f=Figura(2)
print (f)

c=Cuadrado("azul",3,"listo")
print (c)

Color: verde
Lado: 2
Color: azul Lado: 3 Textura: listo

'''

class Color:
  def __init__(self,color):
    self.color=color
  def __str__(self):
    return f"Color: {self.color}"

class Figura:
  def __init__(self,lado):
    self.lado=lado

  def __str__(self):
    return f"Lado: {self.lado}"

class Cuadrado:
  def __init__(self,color,lado,textura):
    self.color=color
    self.lado=lado
    self.textura=textura

  def __str__(self):
    return f"{Color.__str__(self)} {Figura.__str__(self)} Textura: {self.textura}"


c=Color("verde")
print (c)

f=Figura(2)
print (f)

c=Cuadrado("azul",3,"listo")
print (c)