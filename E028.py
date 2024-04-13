'''Pedir una nota del 0 al 10 por teclado que puede tener decimales y transformarla en:
•	Si está entre 9 y 10: imprimir una A
•	Si está entre 8 y menor a 9: imprimir una B
•	Si está entre 7 y menor a 8: imprimir una C
•	Si está entre 6 y menor a 7: imprimir una D
•	Si está entre 0 y menor a 6: imprimir una F
•	Cualquier otro valor debe imprimir: Valor incorrecto
'''
calificacion = int(input("Proporciona una calificación entre 0 y 10: "))
if 9 <= calificacion <= 10:
    print("A")
elif 8 <= calificacion < 9:
    print("B")
elif 7 <= calificacion < 8:
    print("C")
elif 6 <= calificacion < 7:
    print("D")
elif 0 <= calificacion < 6:
    print("F")
else:
    print("Valor desconocido")
