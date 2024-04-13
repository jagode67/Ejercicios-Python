#Pide primero un número por pantalla, a continuación, pide otro número y muestra los siguientes resultados utilizado estos datos: la suma, la resta, la multiplicación, la división, la división entera, el resto de la división (el módulo), y el exponente
opA=input("Primer número: ")
opB=input("Segundo número: ")
#si opA=3 y opB=2 daria los resultado
suma = opA + opB
print(f'Resultado suma: {suma}') #Resultado suma: 5

resta = opA - opB
print(f'Resultado resta: {resta}') #Resultado resta: 1

multi = opA * opB
print(f'Resultado multiplicación: {multi}') #Resultado multiplicación: 6

divi = opA / opB
print(f'Resultado división: {divi}') #Resultado división: 1.5

diviE = opA // opB
print(f'Resultado división entera: {diviE}') #Resultado división entera: 1

modulo = opA % opB
print(f'Resultado módulo: {modulo}') #Resultado módulo: 1

expo = opA ** opB
print(f'Resultado exponente: {expo}') #Resultado exponente: 9
