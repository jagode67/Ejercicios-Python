"""Solicitar un número y escribir una pirámide de números hasta ese número.
Introduce la altura del triángulo: 6
     1
    1 2
   1 2 3
  1 2 3 4
 1 2 3 4 5
1 2 3 4 5 6
"""

altura = int(input("Introduce la altura del triángulo: "))

for i in range(1, altura + 1):
    print(" " * (altura - i), end="")

    for j in range(1, i + 1):
        print(j, end=" ")

    print()