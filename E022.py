#Pedir un número por pantalla y decir si es par, igual a 0 o impar. Utilizar if elif y else.
numero = int(input("Número: "))
if numero ==0:
    print(f"{numero} es 0")
elif numero % 2 == 0:
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")

