# Examen N° 1
# Solucionario Ejercicio N° 2
"""
Una tienda vende alimento para perros de las marcas RICOCAN, DOG CHOW, MIMASKOT
y CANBO. Los precios por kg se muestran a continuación:
Marca       Precio por kg (S/.)
RICOCAN     7.00
DOG CHOW    12.00
MIMASKOT    14.00
CANBO       20.00
Si un cliente compra más de 25 kg de alimento de la marca CANBO, recibe un 10%
de descuento. Por su parte, si compra más de 10 kg de MIMASKOT o DOG CHOW recibe
un 5 % de descuento.
Elabore un programa que solicite al cliente la marca y la cantidad de alimento
(kg) que desea comprar y muestre el descuento aplicado y el precio total a pagar.
Considere que un cliente solo compra alimento de una marca.
"""
marca=input("Ingrese la marca de alimento (RICOCAN, DOG CHOW, MIMASKOT, CANBO): ")
cant=int(input("Ingrese la cantidad (kg) a comprar: "))
desc=0
costo=0
if(marca=="CANBO"):
    costo=20*cant
    if(cant>25):
        desc=0.1*costo
else:
    if(marca=="MIMASKOT"):
        costo=14*cant
        if(cant>10):
            desc=0.05*costo
    else:
        if(marca=="DOG CHOW"):
            costo=12*cant
            if(cant>10):
                desc=0.05*costo
        else:
            costo=7*cant

total=costo-desc
print("Descuento:",desc)
print("Total a pagar:",total)
