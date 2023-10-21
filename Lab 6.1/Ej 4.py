#Lab 6.1
#Ej 4

import random
import math

pi=math.pi
#x=random.random()*pi/2
x=pi/2
print("x=",x)

N=int(input("Ingrese la cantidad de términos: "))
num=1 #pq es el primer termino(inicia todo)
S=num
for c in range (2,N+1):
    
    f=(c-1)*4 ##para que me de el # del factorial
    num=num*(4*x**4)/((f-3)*(f-2)*(f-1)*f)

    ##todos los pares se estan + y los impares se -

    if c%2==0:
        S=S-num
    else:
        S=S+num

print("Suma= ",S)

y=math.cosh(x)* math.cos(x)
print("y=",y)

