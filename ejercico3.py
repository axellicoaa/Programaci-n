# Pedir al usuario un valor. 
# Si el valor es positivo, pedir un segundo valor y calcular la suma, resta y producto de
# ambos. Mostrar los resultados por pantalla.

num1 = int(input("Ingrese numero: "))

if num1 > 0:
    num2 = int(input("Ingrese numero: "))
    suma = num1 + num2
    resta = num1 - num2
    producto = num1 * num2
    print("suma:", suma)
    print("resta:", resta)
    print("producto:", producto)

print("...")