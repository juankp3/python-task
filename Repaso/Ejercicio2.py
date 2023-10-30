# Examen N° 1
# Solucionario Ejercicio N° 2
"""
Una tienda vende alimento para perros de las marcas RICOCAN, DOG CHOW, MIMASKOT y CANBO. 
Los precios por kg se muestran a continuación:
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
marca = input("Ingrese la marca de alimento (RICOCAN, DOG CHOW, MIMASKOT, CANBO): ")
cantidad = int(input("Ingrese la cantidad (kg) a comprar: "))

precios = {
    "RICOCAN" : 7.00,
    "DOG CHOW" : 12.00,
    "MIMASKOT" : 14.00,
    "CANBO" : 20.00,
}
descuento = 0
precio = precios[marca] * cantidad
if (marca == 'CANBO' and cantidad > 25):
    descuento = precio * 0.10

if ((marca == 'MIMASKOT' or marca == 'DOG CHOW')  and cantidad > 10):
    descuento = precio * 0.5

total = precio - descuento



print("Subtotal: ", precio)
print("Descuento: ", descuento)
print("Total a pagar: ", total)


