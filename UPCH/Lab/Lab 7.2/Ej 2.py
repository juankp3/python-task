#Lab 7.2
#Ej 2

##
##N=2
##acum=0
##for i in range (1,N+1):
##    venta=int(input("Venta= "))
##    acum=acum+venta
##print("\nVenta de tienda 1:", acum)
##
##acum=0
##for i in range (1,N+1):
##    venta=int(input("Venta= "))
##    acum=acum+venta
##print("\nVenta de tienda 2:", acum)
##
##acum=0
##for i in range (1,N+1):
##    venta=int(input("Venta= "))
##    acum=acum+venta
##print("\nVenta de tienda 3:", acum)

#con anidamiento

##N=2
##T=3
##montoCiudad=0
##
##print("Ciudad 1")
##for j in range(1,T+1):
##    print("\nTienda ", j)
##    acum=0
##    for i in range (1,N+1):
##        venta=int(input("Venta= "))
##        acum=acum+venta
##    print("\nTotal tienda",j,"=", acum)
##
##    montoCiudad=montoCiudad+acum
##
##print("Total por ciudad=", montoCiudad)
##
##print("\nCiudad 2")
##for j in range(1,T+1):
##    print("\nTienda ", j)
##    acum=0
##    for i in range (1,N+1):
##        venta=int(input("Venta= "))
##        acum=acum+venta
##    print("\nTotal tienda",j,"=", acum)
##
##    montoCiudad=montoCiudad+acum
##
##print("Total por ciudad=", montoCiudad)
##

C=2
N=2
T=3
montoSuc=0
import random 

for k in range(1+C+1):
    print("\nCiudad ", k)
    montoCiudad=0
    for j in range(1,T+1):
        print("\nTienda ", j)
        acum=0
        for i in range (1,N+1):
            venta=random.randint(1000,5000)
            print(venta)
            acum=acum+venta
        print("\nTotal tienda",j,"=", acum)

        montoCiudad=montoCiudad+acum

    print("Total por ciudad ", k,"= ", montoCiudad)
    montoSuc=montoSuc+montoCiudad

print("Recaudación de la Cadena= ", montoSuc)
    
