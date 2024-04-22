'''E094
Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo, la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
print(inversa("cosa"))

'''

def inversa(cadena):
    ret=""
    for i in cadena:
        ret = i+ret
    return ret

print(inversa("cosa"))
