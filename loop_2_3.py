#Calcular el promedio de un alumno que tiene 7 calificaciones en la materia de cálculo


from tkinter import N


# n1 = int(input("Ingrese la nota 1: "))
# n2 = int(input("Ingrese la nota 2: "))
# n3 = int(input("Ingrese la nota 3: "))
# n4 = int(input("Ingrese la nota 4: "))
# n5 = int(input("Ingrese la nota 5: "))
# n6 = int(input("Ingrese la nota 6: "))
# n7 = int(input("Ingrese la nota 7: "))

# suma = (n1+n2+n3+n4+n5+n6+n7)
# promedio = suma/7
# print(promedio, " promedio")

n = 7 
suma= 0
for i in range(n):
    nota =int(input('Ingrese la nota' + str (i+1) +  ':'))
    suma += nota
    
promedio = suma/n 
print("promedio:", promedio)

