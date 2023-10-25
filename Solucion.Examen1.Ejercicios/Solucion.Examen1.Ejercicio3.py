# Examen N° 1
# Solucionario Ejercicio N° 3
"""
Elaborar un programa que lea un número entero positivo de cuatro cifras y
muestre la suma de los dos dígitos del centro. Validar el ingreso, es decir,
si ingresa un número que no tenga 4 dígitos deberá mostrar un mensaje
DATO NO VALIDO.
"""
N=int(input("Ingrese un numero entero positivo de cuatro cifras: "))

if(N>=1000):
    if(N<=9999):
        b=N//100%10
        c=N//10%10
        suma=b+c
        print("La suma de los dos digitos del centro es:",suma)
    else:
        print("DATO NO VALIDO")
else:
    print("DATO NO VALIDO")
