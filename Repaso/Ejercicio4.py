# Examen N° 1
# Solucionario Ejercicio N° 4
"""
Un determinado grado de acero se clasifica de acuerdo con las siguientes
condiciones:
a) La dureza debe ser superior a 50.
b) El contenido de carbono debe ser inferior a 0,7.
c) La resistencia a la tracción debe ser superior a 5600

Las calificaciones son las siguientes:
 La calificación es 10 si se cumplen las tres condiciones.
 La calificación es 9 si se cumplen las condiciones (a) y (b).
 La calificación es 8 si se cumplen las condiciones (b) y (c)
 La calificación es 7 si se cumplen las condiciones (a) y (c)
 La calificación es 6 si solo se cumple una condición
 La calificación es 5 si no se cumple ninguna de las condiciones.
Escriba un programa que solicite el ingreso de los valores de dureza,
contenido de carbono y resistencia a la tracción de un determinado acero y
determine la clasificación del grado del acero.
"""
dureza = int(input("Ingrese la dureza: "))
carbono = float(input("Ingrese el contenido de carbono: "))
resistencia = int(input("Ingrese la resistencia a la tracción: "))

calificacion = 5
if (dureza > 50 and carbono < 0.7 and resistencia > 5600):
    calificacion = 10
elif (dureza > 50 and carbono < 0.7):
    calificacion = 9
elif (carbono < 0.7 and resistencia > 5600):
    calificacion = 8
elif (dureza > 50 and resistencia > 5600):
    calificacion = 7
elif (dureza > 50 or carbono < 0.7 or resistencia > 5600):
    calificacion = 6

print("La clasificación del grado del acero es:", calificacion)