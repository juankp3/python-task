#Lab 4.1
#ej 5

A=int(input("ingrese valor de A: "))
B=int(input("ingrese valor de B: "))

if A>B:
  aux=A
  A=B
  B=aux

num=A
pares=0
impares=0

while num<=B:
  if (num%2==0):
    pares=pares+num
  else:
    impares=impares+num  
  num=num+1

print("La suma de pares es: ",pares)
print("La suma de impares es: ",impares)
