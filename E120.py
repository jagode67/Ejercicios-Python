'''E120
Crear la clase Vendedor con los atributos nombre y ventas. Sobrecargar el operador + para sumar dos vendedores y su resultado sea como nombre “Total” y las ventas, la suma de los dos.
a=Vendedor("Javi",23)
b=Vendedor("María",55)
c=a+b
print(a)
print(b)
print(c)

Nombre: Javi Ventas: 23
Nombre: María Ventas: 55
Nombre: TOTAL Ventas: 78

'''
class Vendedor:
    def __init__(self,nombre,ventas):
        self.nombre=nombre
        self.ventas=ventas

    def __add__(self, other):
        res=Vendedor("TOTAL",self.ventas+other.ventas)
        return(res)

    def __str__(self):
        return f"Nombre: {self.nombre} Ventas: {self.ventas}"

a=Vendedor("Javi",23)
b=Vendedor("María",55)
c=a+b
print(a)
print(b)
print(c)
