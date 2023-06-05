

# num1 = int(input("Ingrese numero: "))
# num2 = int(input("Ingrese numero: "))
# num3 = int(input("Ingrese numero: "))

num1 = 1
num2 = 2
num3 = 3


if num1 < num2:
    num1, num2 = num2, num1

if num1 < num3:
    num1, num3 = num3, num1

if num2 < num3:
    num2, num3 = num3, num2

print('Mayor: ', num1)
print('Medio: ', num2)
print('Menor: ', num3)


# if num1 == num2 and num1 == num3:
#     print(num1)
# if num1>num2 and num1>num3:
#     print(num1)
# elif num2 > num1 and num2 > num3:
#     print(num2)
# elif num3 > num1 and num3 > num2:
#     print(num3)
# elif num1 == num3 or num1 == num2:
#     print(num1)
# elif num2 == num3:
#     print(num2)


