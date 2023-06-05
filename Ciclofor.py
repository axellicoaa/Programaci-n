
# Calcular la suma y la media aritmetica de Nnumeros reales. 
# solicitar el valor de n al usuario y cada uno de los N números reales.

n = int(input("Ingrese los números que desee: "))
suma= 0
for i in range(n):
    nota =int(input('Ingrese el número' + str (i+1) +  ':'))
    suma += nota
    
promedio = suma/n 
print("promedio:", promedio)
print(type(promedio))
