# Calcular el mayor de dos números enteros introducidos por teclado.

# entradas
num1 = int(input("Ingreso num 1: "))
num2 = int(input("Ingreso num 2: "))

# proceso
if num1 > num2:
    # salida
    print("El numero mayor es:", num1)
elif num2 > num1:
    # salida
    print("El numero mayor es:", num2)
else:
    print("Los numeros son iguales")


