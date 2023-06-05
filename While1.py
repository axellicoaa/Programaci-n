

op=1
num1=0
num2=0
while op !=0:

    print ("<1> Sumar")
    print ("<2> Restar")
    print ("<3> Multiplicar")
    print ("<4> Dividir")
    print ("<0> Salir")

    op=int(input("Ingrese opción:"))

    if op !=0:
        num1=int(input("ingrese num1:"))
        num2=int(input("ingrese num2:"))

    if op==1:
        print("Suma:", num1+num2)
    elif op==2:
        print("Resta:", num1-num2)
    elif op==3:
        print("Multiplicación:", num1*num2)
    elif op==4:
        print("División:", num1/num2)

    else:
        print("No existe esa opción")