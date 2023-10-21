#Lab 7.1
#Ej 2

##for num in range (2,13):
##    cdiv=0
##    for i in range(1,num+1):
##        if num%i==0:
##            cdiv= cdiv+1
##    if cdiv==2:
##        print(num," es primo")

#Para encontrar el primo más cercano de un valor definido lim

##lim= 11
##cercano=-1
##for num in range (2,lim):
##    cdiv=0
##    for i in range(1,num+1):
##        if num%i==0:
##            cdiv=cdiv+1
##    if cdiv==2:
##        cercano=num
##if cercano!=-1:
##    print(cercano," es el número primo más cercano")


lim=int(input("Ingrese un número= "))

flag=True
while flag==True:
    lim=lim-1
    cdiv=0
    for num in range(1,lim+1):
        if lim%num==0:
            cdiv=cdiv+1

    if cdiv==2:
        print(lim,"es el último primo")
        flag=False


