#Pedir un número por pantalla y decir por pantalla “uno” si es 1, “dos” si es 2, “tres” si es 3, o “fuera de rango” si es cualquier otro valor. Utilizar if elif y else.
numero = int(input("Número entre 1 y 3:"))

if numero == 1:
    Texto = 'Número uno'
elif numero == 2:
    Texto = 'Número dos'
elif numero == 3:
    Texto = 'Número tres'
else:
    Texto = 'Valor fuera de rango'

print(f'Número: {numero} es: {Texto}')