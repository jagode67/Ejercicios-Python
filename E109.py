'''E109
Crear una clase Aritmética con dos propiedades (operandoA y operandoB) y definir cuatro métodos para operar (sumar, restar, multiplicar, dividir) que retornan el resultado
aritmetica1 = Aritmetica(5, 3)
print(f'Suma: {aritmetica1.sumar()}')
print(f'Resta: {aritmetica1.restar()}')
print(f'Multiplicación: {aritmetica1.multiplicar()}')
print(f'División: {aritmetica1.dividir():.2f}')

Suma: 8
Resta: 2
Multiplicación: 15
División: 1.67

'''


class Aritmetica:
  def __init__(self, operandoA, operandoB):
    self.operandoA = operandoA
    self.operandoB = operandoB

  def sumar(self):
    return self.operandoA + self.operandoB

  def restar(self):
    return self.operandoA - self.operandoB

  def multiplicar(self):
    return self.operandoA * self.operandoB

  def dividir(self):
    return self.operandoA / self.operandoB


aritmetica1 = Aritmetica(5, 3)
print(f'Suma: {aritmetica1.sumar()}')
print(f'Resta: {aritmetica1.restar()}')
print(f'Multiplicación: {aritmetica1.multiplicar()}')
print(f'División: {aritmetica1.dividir():.2f}')
