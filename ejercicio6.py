# Calcular el mayor de cuatro números enteros introducidos por teclado.

num1 = int(input('Ingreso numero: '))
num2 = int(input('Ingreso numero: '))
num3 = int(input('Ingreso numero: '))
num4 = int(input('Ingreso numero: '))

if num1 < num2:
    num1, num2 = num2, num1

if num1 < num3:
    num1, num3 = num3, num1

if num1 < num4:
    num1, num4 = num4, num1

if num2 < num3:
    num2, num3 = num3, num2

if num2 < num4:
    num2, num4 = num4, num2

if num3 < num4:
    num3, num4 = num4, num3

print(num4)
print(num3)
print(num2)
print(num1)