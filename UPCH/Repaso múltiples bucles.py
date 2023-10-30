#Repaso de bucles

#Elabore un programa que:
#Registre y sume las ventas de N trabajadores de una empresa en un día para las M tiendas que tiene la empresa.
#Todas las tiendas tienen la misma cantidad de trabajadores.
#Además, mostrar las ventas totales de la compañía y determinar la tienda que vendió más.

import random

M= int(input("Ingrese la cantidad de tiendas: "))
N=int(input("Ingrese el número de trabajadores: "))

total=0

for t in range(1,M+1):
    print ("\nTienda", t)
    s=0
    
    for i in range (1,N+1):
        print("\nTrabajador",i)
        venta=random.randint(0,500)
        print("Venta:",venta)
        s=s+venta
    print("Suma total de ventas de la tienda en el día:", s)

    total=total+s

    if (t==1):
        mayor=s
        tienda_mayor=t
    else:
        if (s>mayor):
            mayor=s
            tienda_mayor=t

    print("\nVentas totales de la compañía en el día:", total)
    print("Tienda que vendió más:", tienda_mayor, "con", mayor)
