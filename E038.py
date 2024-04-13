# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la suma de todos los números desde 1 hasta ese número.
numero = int(input("Introduce un número entero positivo: "))
suma = 0
while numero > 0:
    suma += numero
    numero -= 1
print("La suma de los números del 1 al", numero, "es", suma)