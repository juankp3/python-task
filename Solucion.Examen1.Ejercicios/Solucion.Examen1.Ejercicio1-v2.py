# Examen N° 1
# Solucionario Ejercicio N° 1
"""
Una compañía de seguros quiere saber cuánto deben pagar en total por la póliza
de una persona. Para calcular la póliza se ingresa una cuota base (de 1 a 500
dólares) y sobre este valor se le carga 7% si la persona bebe alcohol, 4% si
utiliza lentes, si tiene más de 40 años se le carga 13%, de lo contrario sólo 9%.
"""
cuota=int(input("Ingrese la cuota base (1-500 dolares): "))
if (cuota < 1):
    print("La cuota base debe ser de 1 a 500 dólares 1")
    cuota=int(input("Ingrese la cuota base (1-500 dolares): "))
    exit(0)

if (cuota > 500):
    print("La cuota base debe ser de 1 a 500 dólares 2")
    cuota=int(input("Ingrese la cuota base (1-500 dolares): "))
    exit(0)

alcohol=input("¿Bebe alcohol? (si/no): ")
lentes=input("¿Utiliza lentes? (si/no): ")
edad=int(input("Ingrese su edad: "))
pago=cuota



