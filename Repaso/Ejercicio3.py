# Examen N° 1
# Solucionario Ejercicio N° 3
"""
Elaborar un programa que lea un número entero positivo de cuatro cifras y
muestre la suma de los dos dígitos del centro. Validar el ingreso, es decir,
si ingresa un número que no tenga 4 dígitos deberá mostrar un mensaje
DATO NO VALIDO.
"""
numero = input("Ingrese un numero entero positivo de cuatro cifras: ")
# 5793 / 7 + 9 = 16 
# 0123
if (len(numero) == 4):
    suma_numeros = int(numero[1]) + int(numero[2])
    print("La suma de los digitos del medio es: ", suma_numeros)
else:
    print("DATO NO VALIDO")

print("cantidad de caracteres: ", len(numero))

