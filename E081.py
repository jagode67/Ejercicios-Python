'''E081
Crear un diccionario con los valores “María” : 14, “Carlos”: 23 , “Lara”: 18 y mostrar el diccionario ordenado por las claves a través de un for
Carlos
Lara
María

'''
d={"Maria":14, "Carlos":23, "Lara":18}
a=sorted(d.keys())
for k in a:
    print (k)
