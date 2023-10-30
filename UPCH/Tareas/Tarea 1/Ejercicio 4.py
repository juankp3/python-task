#Tarea 1
#Ejercicio 4

elecciones_casa=input("Los tipos de casa son los siguientes: Un piso medianera (A), Dos pisos medianera (B), Un piso esquinera (C), Dos pisos esquinera (D). Presione ENTER para continuar")
tipocasa=input("Ingrese el tipo de casa (un piso medianera, (A/B/C/D): ")
elecciones_acabados=("Los tipos de casa son los siguientes: Obra negra (X), Acabados sencillos (Y), Acabados especiales (Z)")
acabados=int(input("Ingrese los acabados deseados (1/2/3): "))

preciobase=0

if tipocasa=="A":
    if acabados=="X":
        preciobase= 160000
    else:
        if acabados=="Y":
            preciobase= 170000
        else:
            if acabados=="Z":
                preciobase= 175000
        
else:
    if tipocasa=="B":
        if acabados=="X":
            preciobase= 170000
        else:
            if acabados=="Y":
                preciobase= 180000
            else:
                if acabados=="Z":
                    preciobase= 185000
                else:

                    if tipocasa=="C":
                        if acabados=="X":
                            preciobase= 165000
                        else:
                            if acabados=="Y":
                                preciobase= 175000
                            else:
                                if acabados=="Z":
                                    preciobase = 180000
                    else:
                        if tipocasa=="D":
                            if acabados=="X":
                                preciobase= 175000
                            else:
                                if acabados=="Y":
                                    preciobase= 180000
                                else:
                                    if acabados=="Z":
                                        preciobase= 185000

estacionamientos = int(input("Ingrese la cantidad de estacionamientos (0, 1, o 2): "))

preciovivienda = preciobase + estacionamientos*5000

cuotain= 0.3 * preciovivienda
if estacionamientos==2:
    cuotain* 0.9


plazop = int(input("Ingrese el plazo de pago (5, 7, o 10 años): "))

cuotasmen= (preciovivienda - cuotain) / (plazop * 12)

print("Precio de venta de la casa: ", preciovivienda)
print("Años de cuota: ",plazop)
print("Valor de la cuota: ", cuotasmen)
