
# Calcular el promedio de 40 alumnos

import sys


n = 40
suma= 0
menor = sys.maxsize

for i in range(n):
    nota =int(input('Ingrese el número' + str (i+1) +  ':'))
    suma += nota
    if nota < menor:
        menor = nota
    
promedio = suma/n 
print("promedio:", promedio)
print("la nota más baja: ", menor)
