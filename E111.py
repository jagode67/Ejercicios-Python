'''E111
Crear una clase denominada Cubo que se inicializa con ancho, alto y profundo y tendrá
un método que se denomina calcular_volumen() y retorna el volumen del cubo.
El alto, ancho y profundidad se pide por teclado.
Proporciona el ancho: 3
Proporciona el alto: 4
Proprociona lo profundo: 5
Volúmen cubo: 60

'''


class Cubo:
  def __init__(self, ancho, alto, profundo):
    self.ancho = ancho
    self.alto = alto
    self.profundo = profundo

  def calcular_volumen(self):
    return self.ancho * self.alto * self.profundo


ancho = int(input('Proporciona el ancho: '))
alto = int(input('Proporciona el alto: '))
profundo = int(input('Proprociona lo profundo: '))
cubo1 = Cubo(ancho, alto, profundo)
print(f'Volúmen cubo: {cubo1.calcular_volumen()}')