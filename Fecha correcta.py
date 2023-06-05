#Soliciar al usuario una fecha y comprobar si escorrecta. 
#Para que una fecha sea correcta es necesario que:
#El año debe ser mayo que cero.
#El mes debe estar entre 1 y 12
#Dependiendo del mes que sea, el día debe estar dentro de los límites válidos. 
# Los meses que tienen 31 días son 1, 3, 5, 7, 8, 10 y 12. 
# Los meses de 30 días son 4, 6, 9 y 11. El mes de 28 días es 2, excepto en un año bisiesto que es 29 días.

dia = int(input("Ingrese el dia: "))
mes = int(input("Ingrese el mes: "))
anho= int(input("Ingrese el año: "))

if mes<=0 or mes>12 or dia<=0 or dia>31 or anho<0:
    print("La fecha es incorrecta")
elif mes in (1, 3, 5, 7, 8, 10, 12) and dia <=31: 
    print("Fecha correcta")
elif mes in (4, 6, 9, 11) and dia <=30:
    print("Fecha correcta")
elif mes ==2 and dia<=29: 
    if (anho%4==0 and anho%100!=0 or anho%400==0):
        print("Fecha correcta")
    elif dia<=28:
        print("Fecha correcta")
    else:
        print("Fecha incorrecta")
else: 
    print("Fecha incorrecta")
