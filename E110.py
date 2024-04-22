'''E110
Crear una clase denominada Rectángulo que se inicializa con la longitud de la base y de la
altura y tendrá un método que se denomina calcular_area y retorna el área. La base y la altura se pide por teclado

Proporciona la base: 4
Proporciona la altura: 6
Área rectángulo: 24

'''


class Rectangulo:
  def __init__(self, base, altura):
    self.base = base
    self.altura = altura

  def calcular_area(self):
    return self.base * self.altura


base = int(input('Proporciona la base: '))
altura = int(input('Proporciona la altura: '))

rectangulo1 = Rectangulo(base, altura)
print(f'Área rectángulo: {rectangulo1.calcular_area()}')


