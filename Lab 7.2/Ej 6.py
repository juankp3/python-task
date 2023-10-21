#Lab 7.2
#Ej opcional 6

n=8
x=n

for i in range(n):
    for d in range(i,-1,-1):
        print(d, end=" ")
    for f in range (1,x):
        print(f,end=" ")
    x-=1
    print()
