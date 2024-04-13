#Solicitar un mes por pantalla y decir a que estación del año pertenece (del mes 1 al 3: invierno, del mes 4 al 6: primavera, del mes 7 al 9: verano y del mes 10 al 12: otoño)
mes = int(input('Mes del año (1-12): '))

estacion=""
if 1<= mes <=3:
    estacion="Invierto"
elif 4<= mes <=6:
    estacion="Primavera"
elif 7 <= mes <= 9:
    estacion = "Verano"
elif 10<= mes <=12:
    estacion="Otoño"

print(f'Para el mes {mes} la estación es: {estacion}')
