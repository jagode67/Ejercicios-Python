'''E121
Queremos definir una clase abstracta llamada Forma que contenga un método abstracto llamado calcular_area() que deberá ser implementado por las clases concretas que heredan de ella, como Rectangulo y Circulo. Además, queremos definir un método común llamado obtener_nombre() que devuelva el nombre de la forma.
# Crear instancias de las clases
mi_rectangulo = Rectangulo(5, 10)
mi_circulo = Circulo(3)

# Imprimir nombre y área de las formas
print(mi_rectangulo.obtener_nombre())  # Salida: Rectangulo
print(mi_rectangulo.calcular_area())   # Salida: 50
print(mi_circulo.obtener_nombre())     # Salida: Circulo
print(mi_circulo.calcular_area())      # Salida: 28.26

'''
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

    def obtener_nombre(self):
        return self.__class__.__name__

class Rectangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14 * self.radio ** 2

# Crear instancias de las clases
mi_rectangulo = Rectangulo(5, 10)
mi_circulo = Circulo(3)

# Imprimir nombre y área de las formas
print(mi_rectangulo.obtener_nombre())  # Salida: Rectangulo
print(mi_rectangulo.calcular_area())   # Salida: 50
print(mi_circulo.obtener_nombre())     # Salida: Circulo
print(mi_circulo.calcular_area())      # Salida: 28.26

