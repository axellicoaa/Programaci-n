#1.7. Determinar en que estado está el agua en función de su temperatura. Si es negativa el estado será sólido,
#  si es menor que 100 será líquido y si es mayor que 100 será gas. Pedir al usuario el valor de la temperatura.


Temperatura = int(input("Ingrese el valor de la tempertarura en C°:"))
if Temperatura <= 0:
    print("A", Temperatura, "C° el agua está en estado sólido")
elif Temperatura > 0 and Temperatura <= 100:
    print("A", Temperatura, "C° el agua está en estado líquido")
else:
    print("A",Temperatura, "C° el agua está en estado gaseoso")