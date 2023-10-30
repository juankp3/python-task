#Lab 7.2
#Ej opcional 7

cart=input("Ingrese caracter: ")
n=10
x=n
esp= " "

for i in range(n):
    if i==0:
        for d in range(x):
            print(cart, end =" ")
    else:
        for p in range(i-1,-1,-1):
            print(esp, end=" ")
        for d in range(x):
            print(cart, end=" ")
    print()
    x-=1
