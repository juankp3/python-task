# Examen N° 1
# Solucionario Ejercicio N° 1
"""
Una compañía de seguros quiere saber cuánto deben pagar en total por la póliza de una persona. 
Para calcular la póliza se ingresa una cuota base (de 1 a 500 dólares) 
- y sobre este valor se le carga 7% si la persona bebe alcohol, 
- 4% siutiliza lentes,
- si tiene más de 40 años se le carga 13%, de lo contrario sólo 9%.
"""

cuota_base = int(input("Ingrese la cuoda base (entre 1 a 500 dólares): "))
bebe_alchol = input("¿La persona bebe alchol? (Si/No): ").lower()
usa_lentes = input("¿La persona utiliza lentes? (Si/No): ").lower()
edad_persona = int(input("Ingrese le edad de la persona: "))


costo_total = cuota_base
if (cuota_base >= 1 and cuota_base <= 500):

    if (bebe_alchol == "si"):
        costo_total = cuota_base + (cuota_base * 0.07) # 400 + 28

    if (usa_lentes == "si"):
        costo_total = costo_total + (cuota_base * 0.04) # 400 + 16
        # costo_total+= cuota_base * 0.04

    if (edad_persona > 40):
        costo_total = costo_total + (cuota_base * 0.13) # 400 + 52
    else:
        costo_total = costo_total + (cuota_base * 0.09)

    # 400 + 28 +16 + 52: 496
    print("Cuota total de poliza a pagar es: ", costo_total)  
else:
    print("No se puede calcular la poliza")
