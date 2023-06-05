

#Solicitar al usuario la inicial del  día de la semana y mostrar el nombre del día completo.
 #La letra inicial puede ser mayúscula o minúscula. Usar la x para el miércoles.

dia=input('Ingrse el día: ')

if dia=="l" or dia=="L":
    print("Lunes")
elif dia=="m" or dia=="M":
    print("Martes")
elif dia=="x" or dia=="X":
    print("Miércoles")
elif dia=="j" or dia=="J":
    print("Jueves")
elif dia =="v" or dia =="V":
    print(" Viernes")
elif dia=="s" or dia=="S":
    print("Sábado")
elif dia=="d" or dia=="D":
    print(" Domingo")
else:
    print('La inicial es erronea')
