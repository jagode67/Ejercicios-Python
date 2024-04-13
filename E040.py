# Escribir un programa que simule un juego de adivinanzas. El programa debe generar un número aleatorio entre 1 y 100 y el usuario debe intentar adivinarlo. El programa debe dar pistas al usuario sobre si su suposición es mayor o menor que el número aleatorio. Al final debe mostrar en cuantos intentos lo has conseguido adivinar.
# Generar un número aleatorio del 1 al 100
# import random
# numero_aleatorio = random.randint(1, 100)

import random

numero_aleatorio = random.randint(1, 100)

yourNumber = 0
tries=0

while yourNumber != numero_aleatorio:
    yourNumber = int(input("Introduce tu número: "))
    tries+=1

    if yourNumber < numero_aleatorio:
        print("Tu número es menor que el número secreto.")
    elif yourNumber > numero_aleatorio:
        print("Tu número es mayor que el número secreto.")

print(f'¡Felicidades! Has adivinado el número secreto en {tries} intentos.')