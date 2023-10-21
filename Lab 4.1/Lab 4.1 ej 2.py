#Lab 4.1
#Ejercicio 2

N= int(input("Cantidad de datos= "))
cont=1
acum=0

while cont<=N:
    dato=int(input("datos= "))
    acum=acum+dato
    print("acumulador: ", acum)
    cont=cont+1

prom=acum/N
print("El promedio es: ", prom)
