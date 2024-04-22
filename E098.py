'''E098
Crear la función listarTerminos() que recibe como parámetro un diccionario y tiene que mostrar la key y el valor por pantalla.
print(listarTerminos(uno=1,dos=2,tres=3))
print(listarTerminos(nombre="Javi",edad=32,pelo="rubio",ojos="azules"))

'''

def listarTerminos(**terminos):
    for k,v in terminos.items():
        print(f"{k}: {v}")

listarTerminos(uno=1,dos=2,tres=3)
listarTerminos(nombre="Javi",edad=32,pelo="rubio",ojos="azules")
