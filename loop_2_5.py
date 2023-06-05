#leer 10 números e imprimir solamente los positivos.

n=10
for i in range(n):
    num = int(input("Ingrese el número:"))
    if num > 0:
        print(num)
    else:
        print("ingrese números positivos")
    