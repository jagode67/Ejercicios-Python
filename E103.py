'''E103
Definir una función es_palindromo() que reconoce palíndromos
(es decir, palabras que tienen el mismo aspecto escritas invertidas),
ejemplo: es_palindromo ("radar") tendría que devolver True.
es_palindromo("radar")
es_palindromo("coche")

'''


def inversa(cadena):
  ret = ""
  for i in cadena:
    ret = i + ret
  return ret


def es_palindromo(cadena):
  pInv = inversa(cadena)
  if pInv == cadena:
    print("Palindromo")
  else:
    print("No palindromo")


es_palindromo("radar")
es_palindromo("coche")