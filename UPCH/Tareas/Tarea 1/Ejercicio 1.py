#Tarea 1
#Ejercicio 1

costoen= 480
costobio= 700
costomed= 900

print("Las opciones de carreras son las siguientes:")
print("Enfermería, Biología y Medicina")

carelegida = int(input("Ingrese el número de la carrera elegida (1/2/3): "))
hc = int(input("Ingrese el número de horas de crédito que llevará en el semestre: "))

if (carelegida==1):
    costobase=costoen
    carrera="Enfermería"
else:
    if (carelegida==2):
        costobase=costobio
        carrera="Biología"
    else:
        if (carelegida==3):
            costobase=costomed
            carrera="Medicina"
        else:
            print("Opción de carrera no válida.")
    

if hc>24:
    print("No puede llevar más de 24 horas de crédito en un semestre.")

else:

    if hc>20:
        costototal=costobase *hc *1.15
    else:
        costototal=costobase* hc

print("La pensión a pagar por el semestre académico es: ", costototal)


tipodepago = input("Ingrese el tipo de pago (contado/cuotas): ")

if tipodepago=="contado":
    descuento=costototal * 0.10
    montopagar = costototal- descuento
    
    print("Eligió el pago al contado. Tiene un descuento del 10%: ", descuento)
    print("El nuevo monto a pagar es: ", montopagar)
    
else:
    if tipodepago=="cuotas":
        numcuotas= int(input("Ingrese el número de cuotas (4/5): "))
        montoporcuota = costototal/ numcuotas

        print("Eligió el pago en cuotas: ", numcuotas)
        print("El monto a pagar por cuota es: ", montoporcuota)
        print("El monto total a pagar será: ", costototal)

    else:
        print("Opción de pago no válida.")
