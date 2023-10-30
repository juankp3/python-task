#Lab 6.1
#Ej 2

import random
acumc=0
print("\nRegion Centro")
acadc=""
for i in range(1,13):
    pmenc=random.randint(50,150)
    acumc=acumc+pmenc
    acadc=acadc+str(pmenc)+" "
    print("Promedio mensual= ",pmenc)

promarc=acumc/12
print("\nPromedio anual de la Region Centro=",promarc)


acums=0
menor=150
mesmenor=1
acads=""

print("\nRegion Sur")
for i in range(1,13):
    pmens=random.randint(50,150)
    if pmens>menor:
        menor=pmens
        mesmenor=i
    acums=acums+pmens
    acads=acads+str(pmens)+" "
    print("Promedio mensual=",pmens)

promars=acums/12
print("\nPromedio anual de la Region Sur=",promars)
print("\nMes con menos lluvias=", mesmenor, "\nSu registro es=",menor)

acumn=0
acadn=""

print("\nRegion Norte")
for i in range(1,13):
    pmenn=random.randint(50,150)
    acumn=acumn+pmenn
    acadn=acadn+str(pmenn)+" "
    print("Promedio mensual=",pmenn)
promarn=acumn/12
print("\nPromedio anual de la Region Norte=",promarn)

mayor=promarc
region="Centro"

if promarn>mayor:
    mayor=promarn
    region="Norte"

if promars>mayor:
    mayot=promars
    region="Sur"

print("\nRegion=",region, "\nPromedio anual=", mayor)

print("\nRegion Centro")
print(acadc)
print("\nRegion Sur")
print(acads)
print("\nRegion Norte")
print(acadn)
