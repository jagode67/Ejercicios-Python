'''E136
Pedir palabras por pantalla hasta que se pulsa la tecla INTRO. Grabar cada palabra en una línea en un archivo denominado “palabras.txt”

'''

with open("palabras.txt","a",encoding="utf-8") as a:
    while True:
        p=input("Introduce una palabra: ")
        if p=="":
            break
        a.write(p+"\n")

