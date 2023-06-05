#leer 5 números y obtener su cubo y su cuarta.


n= 5
for i in range(n):
    num = int(input("Ingrese el número" + str ( i + 1 )+ ":"))
    print("Cubo", num**3)
    print("cuarta", num**4)   