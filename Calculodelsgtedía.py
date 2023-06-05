#Dada la fecha de hoy
#Calcular la fecha del día siguiente
anho = 2022
mes = 8
dia = 30

if anho % 400 == 0:
        bisiesto = True
elif anho % 4 == 0:
        bisiesto = True

if mes in (1, 3, 5, 7, 8, 10, 12):
        dias_mes = 31
elif mes == 2:
        if bisiesto:
            dias_mes = 29
        else:
            dias_mes = 28
else:
        dias_mes = 30

if dia < dias_mes:
        dia += 1
else:
        dia = 1
        if mes == 12:
            mes = 1
            anho += 1
        else:
            mes += 1
    
  

    
    
print (anho, mes, dia)
