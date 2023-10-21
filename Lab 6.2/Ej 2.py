#Lab 6.2
#Ej 2

import random
LIM=1000
c=1
nAciertos=0

print("      x                   y")
while c<=LIM:
    x=random.random()*2-1
    y=random.random()*2-1
    #Region 1
    if x<=0:
        nAciertos=nAciertos+1
    #Region 3
    else:
        if x<=1:
            if y<=1-x and y>=0:
                nAciertos=nAciertos+1
        
    #print(x, y)
    c=c+1

print("\nNúmero de Aciertos= ", nAciertos)
print("Probabilidad= ", nAciertos/LIM)
