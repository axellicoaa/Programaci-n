
nums=[]
n=5
mayor=0

for i in range(n):
    num= int(input("Digite el número: "))
    nums.append(num)
    if num > mayor:
        mayor=num
        posi=i
print ("El número mayor es:",mayor ,"y se encuentra ubicado en la posición:",posi)