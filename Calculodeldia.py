#Dada la fecha de hoy
#Calcular la fecha del día siguiente

dia = 29
mes = 2
anho = 2020
print(dia, mes, anho)

ultimo_dia = 28

if anho%4 == 0 and anho%100 != 0 or anho%400 == 0:
    ultimo_dia = 29

if mes == 1 or mes==3 or mes == 5 or mes ==7 or mes == 8 or mes == 10 or mes == 12:
    if dia == 31:
        dia = 1
        if mes != 12:
            mes += 1
        elif mes == 12:
            anho += 1
            mes = 1
    else:
        dia += 1
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia == 30:
        dia = 1
        mes += 1
    else:
        dia += 1
elif mes == 2:
    if dia == ultimo_dia:
        dia = 1
        mes += 1
    else:
        dia += 1

print(dia, mes, anho)