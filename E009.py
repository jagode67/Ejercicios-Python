#Pedir por pantalla el alto y el ancho de un rectángulo. Mostrar el área y el perímetro del mismo.
alto = int(input('Proporciona el alto del rectangulo: '))
ancho = int(input('Proporciona el ancho de rectangulo: '))
area = alto * ancho
perimetro = (alto + ancho) * 2
print('Area:', area)
print('Perimetro:', perimetro)
