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
A=int(input("Ingrese la dureza: "))
B=float(input("Ingrese el contenido de carbono: "))
C=int(input("Ingrese la resistencia a la tracción: "))
score=""
if(A>50):
    if(B<0.7):
        if(C>5600):
            score=10
        else:
            score=9
    else:
        if(C>5600):
            score=7
        else:
            score=6     # cumple solo A
else:
    if(B<0.7):
        if(C>5600):
            score=8
        else:
            score=6     # cumple solo B
    else:
        if(C>5600):
            score=6     # cumple solo C
        else:
            score=5
print("La clasificación del grado del acero es:",score)
