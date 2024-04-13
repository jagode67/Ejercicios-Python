#Pedir un número por pantalla y decir si es positivo, igual a 0 o negativo. Utilizar if elif y else.
numero = int(input("Número: "))
if numero ==0:
    print(f"{numero} es 0")
elif numero > 0:
    print(f"{numero} es positivo")
else:
    print(f"{numero} es negativo")

