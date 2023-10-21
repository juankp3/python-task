#Lab 7.2
#Ej 1

#A)

for i in range(1,5):
    j = 0
    while (j < i):
        print(j," ",end="")
        j=j+1

#B)

i = 5;
while (i >= 1):
    num = 1
    for j in range(1,i+1):
        print(num , "*", end=" ")
        num=num*2;

    print()
    i=i-1
        

