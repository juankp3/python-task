# Examen N° 1
# Solucionario Ejercicio N° 1
"""
Una compañía de seguros quiere saber cuánto deben pagar en total por la póliza
de una persona. Para calcular la póliza se ingresa una cuota base (de 1 a 500
dólares) y sobre este valor se le carga 7% si la persona bebe alcohol, 4% si
utiliza lentes, si tiene más de 40 años se le carga 13%, de lo contrario sólo 9%.
"""
cuota=int(input("Ingrese la cuota base (1-500 dolares): "))
alcohol=input("¿Bebe alcohol? (si/no): ")
lentes=input("¿Utiliza lentes? (si/no): ")
edad=int(input("Ingrese su edad: "))
pago=cuota
if(cuota>=1):
    if(cuota<=500):        
        if(alcohol=="si"):
            pago=pago+0.07*cuota
            
        if(lentes=="si"):
            pago=pago+0.04*cuota
            
        if(edad>40):
            pago=pago+0.13*cuota
        else:
            pago=pago+0.09*cuota            
        
        print("Pago por la poliza:", pago)
        
    else: 
        print("La cuota base debe ser de 1 a 500 dólares")
else: 
    print("La cuota base debe ser de 1 a 500 dólares")
