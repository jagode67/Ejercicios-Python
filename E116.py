'''E116
Crear la clase abstracta Figura con los métodos area() y perimetro(). Definir la clase Cuadrado que hereda de Figura.
c=Cuadrado(5)
print(c.area())
print(c.perimetro())

'''

from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Cuadrado(Figura):
    def __init__(self,lado):
        self.lado=lado

    def area(self):
        return(self.lado*self.lado)

    def perimetro(self):
        return(4*self.lado)


c=Cuadrado(5)
print(c.area())
print(c.perimetro())
