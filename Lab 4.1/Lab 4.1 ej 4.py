#Lab 4.1
#ej 4

num=96
s=0
cont=0

while num>=0:
    print(num, end= " ")
    s=s+num
    cont=cont+1
    num=num-2
prom=s/cont

print("\nSuma: ",s)
print("Cantidad de valores: ",cont)
print("promedio= ",prom)
