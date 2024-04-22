'''E092
Escribir la función es_vocal()  que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

print (es_vocal("a"))
print (es_vocal("E"))
print (es_vocal("m"))


'''

def es_vocal(x):
    xM=x.upper()
    if xM=="A" or xM=="E" or xM=="I" or xM=="O" or xM=="U":
        return True
    else:
        return False

print (es_vocal("a"))
print (es_vocal("E"))
print (es_vocal("m"))
