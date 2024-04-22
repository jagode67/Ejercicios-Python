'''E141
Pedir números por pantalla hasta que se introduce un 0. Grabar cada número en una línea en un archivo denominado “numeros.txt”. Si se escribe algo que no sea un número, sacar el mensaje “Solo se admiten números” y volver a pedirlo

'''


with open("numeros.txt","a",encoding="utf-8") as a:
    while True:
        try:
            p=int(input("Introduce un numero: "))
            if p==0:
                break
            a.write(str(p)+"\n")
        except ValueError as e:
            print("Solo se adminten números")

