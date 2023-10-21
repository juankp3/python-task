#Lab 7.2
#Ej 4

ventas = []

total_unidades_por_producto = []
total_unidades_vendidas_por_vendedor = []

dia_max_venta = 0
producto_max_venta_dia = ""
vendedor_max_productos_vendidos_mes = ""
vendedor_max_venta_diaria = ""

for vendedor in range(10):
    ventas_vendedor = []
    for producto in range(5):
        ventas_vendedor.append(0)
        total_unidades_por_producto.append(0)

    ventas.append(ventas_vendedor)
    total_unidades_vendidas_por_vendedor.append(0)

for dia in range(1, 31):
    print(f"=== Día {dia} ===")
    
    for vendedor in range(10):
        print(f"Vendedor {vendedor + 1}:")
        for producto in range(5):
            unidades = int(input(f"Unidades vendidas de Producto {producto + 1}: "))
            ventas[vendedor][producto] += unidades
            total_unidades_por_producto[producto] += unidades
            total_unidades_vendidas_por_vendedor[vendedor] += unidades
            
            if unidades > dia_max_venta:
                dia_max_venta = unidades
                vendedor_max_venta_diaria = vendedor + 1
                producto_max_venta_dia = producto + 1
    
    print("\n")

producto_mas_vendido = total_unidades_por_producto.index(max(total_unidades_por_producto)) + 1

vendedor_max_productos_vendidos_mes = total_unidades_vendidas_por_vendedor.index(max(total_unidades_vendidas_por_vendedor)) + 1

print("=== Resultados ===")
print(f"Total de unidades vendidas por producto durante el mes: {total_unidades_por_producto}")
print(f"Producto con más unidades vendidas durante el mes: Producto {producto_mas_vendido}")
print(f"Vendedor que vendió la mayor cantidad de productos durante el mes: Vendedor {vendedor_max_productos_vendidos_mes}")
print(f"Día con la mayor venta diaria: Día {dia_max_venta}, Vendedor {vendedor_max_venta_diaria}, Producto {producto_max_venta_dia}")
