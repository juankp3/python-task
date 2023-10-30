#Lab 6.1
#Ej 3

import random
LIM=100
i=1
nAciertos=0

print("     x                    y")
for i in range (1,LIM+1):
    x=random.random()*2-1
    y=random.random()*2-1
    print(x,y)
    if x**2+y**2<=1:
        nAciertos=nAciertos+1

piAprox=4*nAciertos/LIM
print("Número de aciertos= ", nAciertos)
print("Pi aproximado", piAprox)
