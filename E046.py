'''E046
Pedir por pantalla un mes y si está entre 1 y 12 decir “mes correcto”, en caso contrario, decir “mes incorrecto”. Utilizar if y range

'''
mes=input("Introdir un mes: ")
if mes in range(1,13):
    print ("mes correcto")
else:
    print ("mes incorrecto")