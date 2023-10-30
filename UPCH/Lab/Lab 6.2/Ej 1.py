#Lab 6.2
#Ej 1

num=int(input("Ingrese un número entero positivo: "))

N=num

inv=0

while N>0:
    r=N%10 #el residuo
    inv=inv*10+r
    N=N//10

print("Inverso: ", inv)

if num==inv:
    print(num,"es capicúa")
else:
    print(num,"no es capicúa")
